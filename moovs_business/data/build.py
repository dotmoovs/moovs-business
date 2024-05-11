import torch
from PIL import Image
from pathlib import Path
import urllib
import requests
import numpy as np
import glob
from moovs.data.utils import IMG_FORMATS, VID_FORMATS
from moovs.utils import downloads


def check_source(source):
    # check if its an image tensor, PIL.Image, np.ndarray, or torch or a path
    if isinstance(source, torch.Tensor):
        tensor = True
        source = source.unsqueeze(0)
    elif isinstance(source, Image.Image):
        from_img = True
    elif isinstance(source, np.ndarray):
        from_img = True
    elif isinstance(source, (str, Path)):
        source = Path(source)
        if source.is_file():
            if source.suffix in IMG_FORMATS:
                from_img = True
            elif source.suffix in VID_FORMATS:
                stream = True
            else:
                raise ValueError("Invalid file format.")
        else:
            if source.is_dir():
                in_memory = True
            else:
                raise ValueError("Invalid source.")
    # download the file if its a link
    elif isinstance(source, str):
        if source.startswith("http"):
            source = downloads.safe_download(source)
            if source.suffix in IMG_FORMATS:
                from_img = True
            elif source.suffix in VID_FORMATS:
                stream = True
            else:
                raise ValueError("Invalid file format.")
        else:
            raise ValueError("Invalid source.")

    else:
        raise ValueError("Invalid source.")

    return source, stream, from_img, in_memory, tensor


def load_inference_source(source=None, batch=1, vid_stride=1, buffer=False):
    """
    Loads an inference source for object detection and applies necessary transformations.

    Args:
        source (str, Path, Tensor, PIL.Image, np.ndarray): The input source for inference.
        batch (int, optional): Batch size for dataloaders. Default is 1.
        vid_stride (int, optional): The frame interval for video sources. Default is 1.
        buffer (bool, optional): Determined whether stream frames will be buffered. Default is False.

    Returns:
        dataset (Dataset): A dataset object for the specified input source.
    """
    source, stream, from_img, in_memory, tensor = check_source(source)

    # Dataloader
    if tensor:
        return source
    elif in_memory:
        dataset = source
    elif stream:
        raise ValueError("Stream not supported.")
    elif from_img:
        # convert to tensor
        source = torch.from_numpy(np.array(source))
    else:
        raise ValueError("Invalid source.")

    return source
