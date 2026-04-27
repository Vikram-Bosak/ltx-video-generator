# 🎬 Text-to-Video Generator

Generate amazing videos from text descriptions using AI!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Text_to_Video_Generator_Fixed.ipynb)

## ✨ Features

- 🎥 **Text-to-Video Generation**: Create videos from simple text prompts
- 🚀 **Easy to Use**: Simple Gradio UI with one-click generation
- ⚡ **Fast**: Optimized for GPU acceleration
- 🎨 **Customizable**: Adjust frames, steps, guidance scale, and more
- 💡 **Example Prompts**: Pre-built examples to get started quickly
- 🔧 **Error Handling**: Comprehensive error messages and troubleshooting

## 🚀 Quick Start

### Option 1: Google Colab (Recommended) ⭐

1. **Click the "Open In Colab" button above**
2. **Enable GPU**: Runtime → Change runtime type → GPU
3. **Run all cells**: Runtime → Run all
4. **Wait for model to load** (3-5 minutes on first run)
5. **Enter your prompt** in the UI
6. **Click "Generate Video"** button
7. **Download your video!**

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/Vikram-Bosak/ltx-video-generator.git
cd ltx-video-generator

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

### Option 3: Jupyter Notebook

```bash
# Clone the repository
git clone https://github.com/Vikram-Bosak/ltx-video-generator.git
cd ltx-video-generator

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook Text_to_Video_Generator_Fixed.ipynb
```

## ⚙️ Requirements

- **Python**: 3.8+
- **GPU**: NVIDIA GPU with 8GB+ VRAM (recommended)
- **CUDA**: 11.8+
- **RAM**: 16GB+ recommended
- **Storage**: 10GB+ free space

## 📦 Dependencies

```
torch>=2.0.0
torchvision>=0.15.0
transformers>=4.30.0
diffusers>=0.20.0
accelerate>=0.20.0
gradio>=3.50.0
xformers>=0.0.20 (optional)
opencv-python>=4.8.0
imageio-ffmpeg>=0.4.0
```

## 🎯 How to Use

### Step-by-Step Guide:

1. **Enable GPU Runtime**
   - Click "Runtime" in the menu
   - Select "Change runtime type"
   - Choose "GPU" as hardware accelerator
   - Click "Save"

2. **Install Dependencies**
   - Run the installation cell
   - Wait for all packages to install

3. **Load the Model**
   - Run the model loading cell
   - Wait 3-5 minutes for first run
   - Model will be cached for future runs

4. **Generate Video**
   - Enter your text prompt
   - Adjust settings if needed
   - Click "Generate Video"
   - Wait 1-3 minutes for generation
   - Download your video!

### Settings Explained:

- **Number of Frames**: How many frames in the video (8-32)
  - More frames = longer video but slower generation
  
- **Inference Steps**: How many denoising steps (10-50)
  - More steps = better quality but slower generation
  
- **Guidance Scale**: How closely to follow prompt (1.0-15.0)
  - Higher = more faithful to prompt
  - Lower = more creative/abstract
  
- **Seed**: Random seed for reproducibility
  - -1 = random (default)
  - Set a number for reproducible results
  
- **FPS**: Frames per second (4-16)
  - Higher = smoother video but larger file

## 💡 Example Prompts

### Simple Prompts:
- "A sunset over the ocean"
- "A cat playing with a ball"
- "Rain falling on a window"

### Medium Prompts:
- "A beautiful sunset over the ocean with waves"
- "A cute cat playing with a red ball in a garden"
- "Rain falling gently on a window at night"

### Detailed Prompts:
- "A cinematic sunset over the Pacific Ocean, with golden waves gently rolling onto a sandy beach, seagulls flying in the distance"
- "A fluffy orange cat playing with a bright red ball in a sunny garden, with flowers blooming all around"
- "Rain falling gently on a window at night, with city lights reflecting in the droplets, creating a cozy atmosphere"

### Creative Prompts:
- "A serene Japanese garden with cherry blossoms falling gently, koi fish swimming in a crystal clear pond"
- "An astronaut floating in space with Earth in the background, cinematic lighting"
- "A magical forest with glowing mushrooms and fireflies at night, fantasy style"
- "Ocean waves crashing on a rocky beach during golden hour, slow motion"
- "A cute robot exploring a colorful alien planet, animated style"

## 📊 Performance

| GPU | VRAM | Generation Time (16 frames) | Quality |
|-----|------|----------------------------|---------|
| T4  | 16GB | ~3-5 minutes | Good |
| V100 | 32GB | ~2-3 minutes | Excellent |
| A100 | 40GB | ~1-2 minutes | Excellent |

**Note:** First generation takes longer due to model download.

## 🐛 Troubleshooting

### Common Issues:

1. **"CUDA out of memory"**
   - Reduce number of frames
   - Reduce inference steps
   - Restart runtime

2. **"No GPU detected"**
   - Enable GPU in runtime settings
   - Restart runtime

3. **Model loading takes too long**
   - First run always takes 3-5 minutes
   - Be patient, model is being downloaded
   - Subsequent runs will be faster

4. **Video generation fails**
   - Make sure GPU is enabled
   - Try a simpler prompt
   - Reduce number of frames
   - Restart runtime

For detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

## 📝 Model Information

**Model**: ModelScope Text-to-Video MS 1.7B
**Developer**: Alibaba DAMO Academy
**License**: Apache 2.0
**Framework**: Diffusers
**Model Size**: ~3GB

## 🎨 Tips for Better Results

### Writing Good Prompts:

1. **Be Specific**: Describe what you want to see
   - ✅ "A red car driving on a highway"
   - ❌ "A car"

2. **Add Details**: Include colors, lighting, atmosphere
   - ✅ "A red sports car driving on a coastal highway at sunset"
   - ❌ "A car on a road"

3. **Use Descriptive Words**: Adjectives and adverbs help
   - ✅ "Gently flowing river with crystal clear water"
   - ❌ "River flowing"

4. **Set the Scene**: Describe the environment
   - ✅ "A cozy cabin in a snowy forest during winter"
   - ❌ "A cabin"

### Negative Prompts:

Use negative prompts to avoid unwanted elements:
- "blurry, low quality, distorted, ugly, bad animation"
- "watermark, text, logo, signature"
- "bad anatomy, deformed, disfigured"

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Alibaba DAMO Academy](https://modelscope.cn/) for the text-to-video model
- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Gradio](https://gradio.app/) for the UI framework

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🔗 Links

- **GitHub Repository**: https://github.com/Vikram-Bosak/ltx-video-generator
- **Colab Notebook**: https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Text_to_Video_Generator_Fixed.ipynb
- **Model**: https://huggingface.co/damo-vilab/text-to-video-ms-1.7b
- **Troubleshooting**: [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

**Made with ❤️ by Vikram Bosak**

**Note**: This tool uses the ModelScope text-to-video model. Please respect the model's license and terms of use.

## 📈 Changelog

### Version 2.0 (Fixed)
- ✅ Fixed all import errors
- ✅ Added comprehensive error handling
- ✅ Improved model loading
- ✅ Added troubleshooting guide
- ✅ Better memory management
- ✅ More reliable video generation

### Version 1.0
- Initial release
- Basic text-to-video generation
- Simple Gradio UI
