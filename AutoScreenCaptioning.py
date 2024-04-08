from transformers import BlipProcessor, BlipForConditionalGeneration
from torch.cuda import is_available
import utils

CUDA_device = "cuda:0" if is_available() else "cpu"
model_path = "cache/models--Salesforce--blip-image-captioning-large/snapshots/2227ac38c9f16105cb0412e7cab4759978a8fd90"
model_name = "Salesforce/blip-image-captioning-large"

class auto_screen_captioning():
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained(model_path, local_files_only=True) if utils.find(model_path, "preprocessor_config.json") else BlipProcessor.from_pretrained(model_name, cache_dir="cache")
        self.model = BlipForConditionalGeneration.from_pretrained(model_path, local_files_only=True).to(CUDA_device) if utils.find(model_path, "config.json") else BlipForConditionalGeneration.from_pretrained(model_name, cache_dir="cache").to(CUDA_device)

    def image_caption(self, path):
        img = utils.get_image(path)
        text = "a photography of"
        inputs = self.processor(img, text, return_tensors="pt")
        inputs.to("cuda:0")
        output = self.model.generate(**inputs)

        return self.processor.decode(output[0], skip_special_tokens=True)
    
    def auto_screen_caption(self):
        path = utils.take_screenshot()
        return self.image_caption(path)
