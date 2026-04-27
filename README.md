# 🎬 LTX-Video Text-to-Video Generator

Generate amazing videos from text descriptions using LTX-Video (LTX 2.3) model!

## ✨ Features

- 🎥 **Text-to-Video Generation**: Create videos from simple text prompts
- 🚀 **Easy to Use**: Simple Gradio UI with one-click generation
- ⚡ **Fast**: Optimized for GPU acceleration
- 🎨 **Customizable**: Adjust frames, steps, guidance scale, and more
- 💡 **Example Prompts**: Pre-built examples to get started quickly

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

1. Open the notebook in Google Colab
2. Change runtime to GPU (Runtime → Change runtime type → GPU)
3. Run all cells
4. Use the UI to generate videos

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/LTX_Video_Generator.ipynb)

### Option 2: Local Setup

```bash
# Clone the repository
git clone https://github.com/Vikram-Bosak/ltx-video-generator.git
cd ltx-video-generator

# Install dependencies
pip install torch torchvision torchaudio
pip install transformers diffusers accelerate gradio xformers

# Run the notebook
jupyter notebook LTX_Video_Generator.ipynb
```

## ⚙️ Requirements

- **Python**: 3.8+
- **GPU**: NVIDIA GPU with 8GB+ VRAM (recommended)
- **CUDA**: 11.8+
- **RAM**: 16GB+ recommended

## 📦 Dependencies

```
torch>=2.0.0
torchvision>=0.15.0
transformers>=4.30.0
diffusers>=0.20.0
accelerate>=0.20.0
gradio>=3.50.0
xformers>=0.0.20
```

## 🎯 How to Use

1. **Enter your prompt**: Describe the video you want to create
2. **Adjust settings** (optional):
   - Number of frames (9-121)
   - Inference steps (10-50)
   - Guidance scale (1.0-10.0)
   - Seed for reproducibility
   - FPS (8-60)
3. **Click "Generate Video"**
4. **Download your video**!

## 💡 Example Prompts

- "A serene Japanese garden with cherry blossoms falling gently, koi fish swimming in a crystal clear pond"
- "An astronaut floating in space with Earth in the background, cinematic lighting"
- "A magical forest with glowing mushrooms and fireflies at night, fantasy style"
- "Ocean waves crashing on a rocky beach during golden hour, slow motion"
- "A cute robot exploring a colorful alien planet, animated style"

## 🎨 Advanced Settings

### Number of Frames
- **Range**: 9-121 frames
- **Default**: 49 frames
- **More frames** = Longer video but slower generation

### Inference Steps
- **Range**: 10-50 steps
- **Default**: 20 steps
- **More steps** = Better quality but slower generation

### Guidance Scale
- **Range**: 1.0-10.0
- **Default**: 2.5
- **Higher** = More faithful to prompt
- **Lower** = More creative/abstract

### Seed
- **Default**: -1 (random)
- **Set a number** for reproducible results

### FPS
- **Range**: 8-60
- **Default**: 24
- **Higher** = Smoother video but larger file

## 📊 Performance

| GPU | VRAM | Generation Time (49 frames) |
|-----|------|----------------------------|
| T4  | 16GB | ~2-3 minutes |
| V100 | 32GB | ~1-2 minutes |
| A100 | 40GB | ~30-60 seconds |

## 🐛 Troubleshooting

### Out of Memory Error
- Reduce number of frames
- Reduce batch size
- Use a smaller model variant

### Slow Generation
- Check GPU is being used
- Reduce inference steps
- Reduce number of frames

### Poor Quality
- Increase inference steps
- Adjust guidance scale
- Improve your prompt

## 📝 Model Information

**Model**: LTX-Video (LTX 2.3)
**Developer**: Lightricks
**License**: Apache 2.0
**Paper**: [LTX-Video: Efficient Video Generation with Latent Diffusion](https://arxiv.org/abs/2409.06571)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Lightricks](https://github.com/Lightricks) for the LTX-Video model
- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Gradio](https://gradio.app/) for the UI framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Made with ❤️ by Vikram Bosak**

**Note**: This tool uses the LTX-Video model from Lightricks. Please respect the model's license and terms of use.
