from dataclasses import dataclass

DEFAULT_MODEL = "SD-1.5"
DEFAULT_SAMPLER = "k_dpmpp_2m"

DEFAULT_NEGATIVE_PROMPT = (
    "weird eyes, smudged face, blurred face, poorly drawn face, mutation, mutilation, cloned face, strange mouth, "
    "Ugly, duplication, duplicates, mutilation, deformed, mutilated, mutation, twisted body, disfigured, bad anatomy, "
    "poorly drawn hands, extra limbs, malformed limbs, missing arms, extra arms, missing legs, extra legs, mutated hands, "
    "extra hands, fused fingers, missing fingers, extra fingers, long neck, small head, closed eyes, rolling eyes, "
    "grainy, blurred, blurry, writing, calligraphy, signature, text, watermark, bad art, "
    "out of frame, extra fingers, mutated hands, porn, child abuse, horrific images, dead bodies"
)


@dataclass
class ModelConfig:
    short_name: str
    config_path: str
    weights_url: str
    default_image_size: int
    forced_attn_precision: str = "default"


midas_url = "https://github.com/intel-isl/DPT/releases/download/1_0/dpt_hybrid-midas-501f0c75.pt"

MODEL_CONFIGS = [
    ModelConfig(
        short_name="SD-1.4",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/bstddev/sd-v1-4/resolve/77221977fa8de8ab8f36fac0374c120bd5b53287/sd-v1-4.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-1.5",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/acheong08/SD-V1-5-cloned/resolve/fc392f6bd4345b80fc2256fa8aded8766b6c629e/v1-5-pruned-emaonly.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-1.5-inpaint",
        config_path="configs/stable-diffusion-v1-inpaint.yaml",
        weights_url="https://huggingface.co/julienacquaviva/inpainting/resolve/2155ff7fe38b55f4c0d99c2f1ab9b561f8311ca7/sd-v1-5-inpainting.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-2.0",
        config_path="configs/stable-diffusion-v2-inference.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-base/resolve/main/512-base-ema.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-2.0-inpaint",
        config_path="configs/stable-diffusion-v2-inpainting-inference.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-inpainting/resolve/main/512-inpainting-ema.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-2.1",
        config_path="configs/stable-diffusion-v2-inference.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-1-base/resolve/main/v2-1_512-ema-pruned.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-2.1-inpaint",
        config_path="configs/stable-diffusion-v2-inpainting-inference.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-inpainting/resolve/main/512-inpainting-ema.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SD-2.1-v",
        config_path="configs/stable-diffusion-v2-inference-v.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt",
        default_image_size=768,
        forced_attn_precision="fp32",
    ),
    ModelConfig(
        short_name="SD-2.0-v",
        config_path="configs/stable-diffusion-v2-inference-v.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2/resolve/main/768-v-ema.ckpt",
        default_image_size=768,
    ),
    ModelConfig(
        short_name="SD-2.0-depth",
        config_path="configs/stable-diffusion-v2-midas-inference.yaml",
        weights_url="https://huggingface.co/stabilityai/stable-diffusion-2-depth/resolve/main/512-depth-ema.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="MidJourney-PaperCut",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/ShadoWxShinigamI/MidJourney-PaperCut/resolve/main/Mdjrny-pprct_step_7000.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="Openjourney",
        config_path="configs/stable-diffusion-v1.yaml",
        # weights_url="https://civitai.com/api/download/models/96",
        weights_url="https://huggingface.co/prompthero/openjourney-v2/resolve/main/openjourney-v2-unpruned.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="Protogen-Anime",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://civitai.com/api/download/models/4007",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="Protogen-Photo",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/darkstorm2150/Protogen_x3.4_Official_Release/resolve/main/ProtoGen_X3.4.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="Protogen-PhotoV2",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/darkstorm2150/Protogen_v5.3_Official_Release/resolve/main/ProtoGen_X5.3.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="RPG",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/Anashel/rpg/resolve/main/RPG-v2.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="SynthwavePunk",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/zipp425/synthwavePunk/resolve/main/synthwavePunk_v2.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="ModernDisney",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/nitrosocke/mo-di-diffusion/resolve/main/moDi-v1-pruned.ckpt",
        default_image_size=512,
    ),
    ModelConfig(
        short_name="ModernBuildings_SD21",
        # config_path="configs/stable-diffusion-v2-inference-v.yaml",
        config_path="configs/stable-diffusion-v2-modern-buildings.yaml",
        weights_url="https://huggingface.co/smereces/2.1-SD-Modern-Buildings-Style-MD/resolve/main/midjourneyi_16500_lora.ckpt",
        default_image_size=768,
    ),
    ModelConfig(
        short_name="DreamLikeHumans",
        config_path="configs/stable-diffusion-v1.yaml",
        weights_url="https://huggingface.co/dreamlike-art/dreamlike-photoreal-2.0/resolve/main/dreamlike-photoreal-2.0.ckpt",
        default_image_size=512,
    ),
    # ModelConfig(
    #     short_name="SD-2.0-upscale",
    #     config_path="configs/stable-diffusion-v2-upscaling.yaml",
    #     weights_url="https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler/resolve/main/x4-upscaler-ema.ckpt",
    #     default_image_size=512,
    # ),
]

MODEL_CONFIG_SHORTCUTS = {m.short_name: m for m in MODEL_CONFIGS}

MODEL_SHORT_NAMES = sorted(MODEL_CONFIG_SHORTCUTS.keys())
