# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. "CUDA out of memory" Error

**Problem:**
```
RuntimeError: CUDA out of memory. Tried to allocate X GB
```

**Solutions:**
- ✅ Reduce number of frames (try 8 instead of 16)
- ✅ Reduce inference steps (try 15 instead of 25)
- ✅ Restart the runtime to clear memory
- ✅ Use a smaller model variant if available

**How to restart:**
```
Runtime → Restart runtime
```

---

### 2. "No module named 'xformers'" Error

**Problem:**
```
ModuleNotFoundError: No module named 'xformers'
```

**Solution:**
- ✅ This is NOT critical - the code will work without it
- ✅ The notebook will use default attention instead
- ✅ Performance will be slightly slower but still functional

**To install xformers (optional):**
```python
!pip install xformers
```

---

### 3. Model Loading Takes Too Long

**Problem:**
- Model loading seems stuck
- Taking more than 10 minutes

**Solution:**
- ✅ First run ALWAYS takes 3-5 minutes (model download)
- ✅ Be patient, the model is being downloaded from HuggingFace
- ✅ Subsequent runs will be much faster (model is cached)
- ✅ Check your internet connection

**What's happening:**
- Model size: ~3GB
- Download speed depends on your connection
- After first download, model is cached locally

---

### 4. Video Generation Fails

**Problem:**
- Generation starts but fails midway
- Error during video creation

**Solutions:**
- ✅ Make sure GPU is enabled (Runtime → Change runtime type → GPU)
- ✅ Try a simpler prompt
- ✅ Reduce the number of frames
- ✅ Restart the runtime
- ✅ Check VRAM availability

**How to enable GPU:**
```
Runtime → Change runtime type → Hardware accelerator → GPU
```

---

### 5. "Connection reset" or Timeout Errors

**Problem:**
```
ConnectionResetError: [Errno 104] Connection reset by peer
TimeoutError: Request timed out
```

**Solution:**
- ✅ This is normal for large model downloads
- ✅ Wait a few minutes and try again
- ✅ The model will be cached after first download
- ✅ Check your internet connection

---

### 6. "AttributeError: module 'diffusers' has no attribute"

**Problem:**
```
AttributeError: module 'diffusers' has no attribute 'export_to_video'
```

**Solution:**
- ✅ Update diffusers to latest version
- ✅ Restart runtime after update

**How to update:**
```python
!pip install --upgrade diffusers
```

---

### 7. GPU Not Detected

**Problem:**
```
🎯 Using device: cpu
⚠️  Warning: No GPU detected
```

**Solution:**
- ✅ Enable GPU in runtime settings
- ✅ Restart runtime after enabling GPU
- ✅ Make sure you're using a GPU runtime

**How to enable:**
```
Runtime → Change runtime type → Hardware accelerator → GPU → Save
```

---

### 8. Import Errors

**Problem:**
```
ImportError: cannot import name 'X' from 'Y'
```

**Solution:**
- ✅ Run the installation cell first
- ✅ Restart runtime after installation
- ✅ Make sure all packages are installed

**Installation cell:**
```python
!pip install -q --upgrade torch torchvision torchaudio
!pip install -q --upgrade transformers diffusers accelerate gradio
!pip install -q --upgrade xformers
!pip install -q opencv-python imageio-ffmpeg
```

---

### 9. Video File Not Created

**Problem:**
- Generation completes but no video file
- Video path doesn't exist

**Solution:**
- ✅ Check the output path in the status message
- ✅ Look in `/content/` directory
- ✅ Try generating again with different settings
- ✅ Check for error messages in the output

---

### 10. Gradio Interface Not Loading

**Problem:**
- Gradio interface doesn't appear
- "Running on public URL" but no interface

**Solution:**
- ✅ Wait 10-20 seconds for interface to load
- ✅ Check if there are any error messages
- ✅ Try refreshing the page
- ✅ Make sure all cells ran successfully

---

## Performance Tips

### For Faster Generation:
1. ✅ Use fewer frames (8-12 instead of 16-32)
2. ✅ Use fewer inference steps (15-20 instead of 25-50)
3. ✅ Use a GPU with more VRAM
4. ✅ Close other tabs/applications using GPU

### For Better Quality:
1. ✅ Use more inference steps (30-50)
2. ✅ Use higher guidance scale (8-12)
3. ✅ Write detailed, specific prompts
4. ✅ Use appropriate negative prompts

### For Lower Memory Usage:
1. ✅ Use fewer frames
2. ✅ Use fewer inference steps
3. ✅ Restart runtime periodically
4. ✅ Clear cache between generations

---

## Quick Reference

### Minimum Requirements:
- **GPU**: NVIDIA with 8GB+ VRAM
- **RAM**: 16GB+ recommended
- **Storage**: 10GB+ free space
- **Python**: 3.8+

### Recommended Settings:
- **Frames**: 16 (for balance)
- **Steps**: 25 (for quality)
- **Guidance**: 7.5 (for fidelity)
- **FPS**: 8 (for smoothness)

### Example Prompts:
```
Simple: "A sunset over the ocean"
Medium: "A beautiful sunset over the ocean with waves"
Detailed: "A cinematic sunset over the Pacific Ocean, with golden waves gently rolling onto a sandy beach, seagulls flying in the distance"
```

---

## Getting Help

### Before Asking for Help:
1. ✅ Check GPU is enabled
2. ✅ Check all cells ran successfully
3. ✅ Check error messages carefully
4. ✅ Try restarting the runtime
5. ✅ Try with default settings

### Information to Provide:
- Error message (full text)
- GPU model and VRAM
- Settings used (frames, steps, etc.)
- Prompt used
- Which cell failed

### Where to Get Help:
- GitHub Issues: https://github.com/Vikram-Bosak/ltx-video-generator/issues
- Check the README.md for more information
- Review the troubleshooting steps above

---

## Success Checklist

Before generating your first video, make sure:

- [ ] GPU is enabled (Runtime → Change runtime type → GPU)
- [ ] All installation cells ran successfully
- [ ] Model loaded without errors
- [ ] GPU is detected in the output
- [ ] You have at least 8GB VRAM
- [ ] You have a stable internet connection
- [ ] You've read the example prompts

---

## Common Mistakes to Avoid

❌ **Don't:**
- Skip the installation cells
- Use CPU runtime
- Try to generate with 100+ frames
- Use extremely long prompts
- Interrupt model loading

✅ **Do:**
- Run all cells in order
- Enable GPU runtime
- Start with default settings
- Use example prompts first
- Be patient during first run

---

**Last Updated:** April 27, 2026

**Note:** This guide is continuously updated. If you encounter an issue not listed here, please open a GitHub issue.
