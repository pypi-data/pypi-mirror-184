
import numpy as np
from torchvision.utils import make_grid
from PIL import Image
import torch
from pytorch_lightning.callbacks import Callback
import os
from pathlib import Path
from pytorch_lightning.utilities import rank_zero_only

from huggingface_hub import HfApi
from dotenv import load_dotenv

#from omegaconf import ListConfig
#from diffusers.configuration_utils import FrozenDict

class ImageLogger(Callback):
    def __init__(self, 
        steps_per_sample=1000, 
        batch_size=4, 
        base_dir=None, 
        sample_dir_name='samples',
        init_key = 'init',
        cond_key = 'cond',
        image_key = 'image'
    ):
        super().__init__()
        vars(self).update(locals())
        
    def init_directories(self, base_dir):
        self.base_dir = Path(base_dir)
        self.samples_dir = self.base_dir/self.sample_dir_name
        os.makedirs(self.base_dir, exist_ok=True)
        os.makedirs(self.samples_dir, exist_ok=True)

    @rank_zero_only
    def on_train_batch_end(self, trainer, pl_module, outputs, batch, batch_idx):
        self.log_images(trainer, pl_module, outputs, batch, batch_idx)

    #@rank_zero_only
    #def on_validation_batch_end(self, trainer, pl_module, outputs, batch, batch_idx, dataloader_idx):
    #    self.log_images(trainer, pl_module, outputs, batch, batch_idx)


    def log_images(self, trainer, pl_module, outputs, batch, batch_idx):

        if batch_idx % self.steps_per_sample == 0:
            if self.base_dir is None:
                self.init_directories(trainer.log_dir)
            save_path = self.samples_dir/f'{trainer.global_step}.png'

            image_tensors = self.process_tensors(pl_module, outputs, batch)

            batch_size = batch[self.image_key].shape[0]
            save_images(image_tensors, save_path, nrows=batch_size)


    def process_tensors(self, pl_module, outputs, batch):
        
        input_tensors = batch[self.image_key]
        if self.init_key in batch:
            input_tensors = torch.cat([batch[self.init_key], batch[self.image_key]], dim=0)
        input_tensors = (input_tensors / 2 + 0.5).clamp(0, 1).cpu()

        pred_tensors = self.get_predictions(pl_module, outputs, batch)
        return torch.cat([input_tensors, pred_tensors])

    # overwrite in inheriting class to define how to obtain predicted images
    # by default logs only the input images
    def get_predictions(self, pl_module, outputs):
        return torch.tensor([])



# save model weights locally using huggingface save_pretrained method
# if HF_API_KEY key defined in environment, also upload the model weights to huggingface hub
class SavePretrained(Callback):
    def __init__(self, repo_name='test', model_key='unet', output_dir='models/unet', every_n_epochs=20):
        super().__init__()
        vars(self).update(locals())

        load_dotenv()
        HF_API_KEY = os.getenv('HF_API_KEY')
        self.api = HfApi(token=HF_API_KEY) if HF_API_KEY is not None else None

        if self.api is not None:
            self.repo_url = self.api.create_repo(repo_id=repo_name, private=True, exist_ok=True)
            self.user_info = self.api.whoami()

    def save_model(self, trainer, pl_module):

        model = getattr(pl_module, self.model_key)

        # must convert omegaconf ListConfig to list for json serialization 
        # or patch to_json_saveable in diffusers.configuration_utils
        #if hasattr(model, '_internal_dict'):
        #    model._internal_dict = FrozenDict({k: list(v) if isinstance(v, ListConfig) else v for k, v in model._internal_dict.items()})
        model.save_pretrained(self.output_dir)

        if self.api is not None:
            self.saved_model_url = self.api.upload_folder(
                folder_path=self.output_dir,
                path_in_repo=self.model_key,
                repo_id=f"{self.user_info['name']}/{self.repo_name}",
                repo_type="model",
            )
        
    @rank_zero_only
    def on_train_epoch_end(self, trainer, pl_module):
        if pl_module.current_epoch % self.every_n_epochs == (self.every_n_epochs - 1):
            self.save_model(trainer, pl_module)



# packs keyword arguments into a list
class ArgsList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(args + tuple(kwargs.values()))


# save pytorch image tensors (of shape B x C x H x W) to image files in save_path
# input tensors expected to be in range [0, 1]
def save_images(image_tensors, save_path=None, nrows=4):

    grid = make_grid(image_tensors.detach().cpu(), normalize=False, nrow=nrows)
    grid = grid.permute(1,2,0).squeeze(-1)*255
    grid = grid.numpy().astype(np.uint8)

    image_grid = Image.fromarray(grid)
    if save_path is not None: image_grid.save(save_path)

    return image_grid

