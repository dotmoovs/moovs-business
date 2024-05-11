import os

IMG_FORMATS = {
    "bmp",
    "dng",
    "jpeg",
    "jpg",
    "mpo",
    "png",
    "tif",
    "tiff",
    "webp",
    "pfm",
}  # image suffixes
VID_FORMATS = {
    "asf",
    "avi",
    "gif",
    "m4v",
    "mkv",
    "mov",
    "mp4",
    "mpeg",
    "mpg",
    "ts",
    "wmv",
    "webm",
}  # video suffixes
PIN_MEMORY = (
    str(os.getenv("PIN_MEMORY", True)).lower() == "true"
)  # global pin_memory for dataloaders
FORMATS_HELP_MSG = (
    f"Supported formats are:\nimages: {IMG_FORMATS}\nvideos: {VID_FORMATS}"
)
