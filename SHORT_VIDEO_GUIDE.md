# Short Video Generator - Quick Guide

## 🎯 What This Does

Generate short vertical videos perfect for:
- YouTube Shorts
- Facebook Reels
- Instagram Reels
- TikTok
- WhatsApp Status

## ⚡ Why This Version?

**Optimized for Speed & Stability:**
- ✅ Fewer frames (6-12 instead of 16-32)
- ✅ Fewer steps (10-20 instead of 25-50)
- ✅ Lower memory usage
- ✅ Faster generation (1-2 minutes)
- ✅ Less likely to crash

## 🚀 How to Use

### Step 1: Open Notebook
```
https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Short_Video_Generator.ipynb
```

### Step 2: Enable GPU
1. Click "Runtime" in top menu
2. Click "Change runtime type"
3. Select "GPU" as hardware accelerator
4. Click "Save"

### Step 3: Run All Cells
1. Click "Runtime" in top menu
2. Click "Run all"
3. Wait 2-3 minutes for model to load

### Step 4: Generate Video
1. Enter your prompt (keep it simple!)
2. Click "Generate Short Video"
3. Wait 1-2 minutes
4. Download your video!

## 💡 Example Prompts

### Simple (Recommended):
- "A sunset over the ocean"
- "A cat playing with a ball"
- "Rain falling on a window"
- "Flowers blooming"
- "A bird flying"

### Medium:
- "A beautiful sunset over the ocean with waves"
- "A cute cat playing with a red ball"
- "Rain falling gently on a window"

### Detailed (May be slower):
- "A cinematic sunset over the ocean with golden waves"

## ⚙️ Recommended Settings

| Setting | Value | Why |
|---------|-------|-----|
| Frames | 8 | Balance between length and speed |
| Steps | 15 | Good quality without being slow |
| Guidance | 7.5 | Follows prompt well |
| FPS | 8 | Smooth playback |

**Result:** ~1 second video, 1-2 minutes generation time

## 🐛 Common Issues

### Issue: Notebook crashes
**Solution:**
- Reduce frames to 6
- Reduce steps to 10
- Restart runtime

### Issue: "No GPU detected"
**Solution:**
- Enable GPU (Runtime → Change runtime type → GPU)
- Restart runtime

### Issue: Model loading takes too long
**Solution:**
- First run always takes 2-3 minutes
- Be patient, model is being downloaded
- Subsequent runs will be faster

### Issue: Video not generating
**Solution:**
- Check GPU is enabled
- Wait 2-3 minutes for first run
- Try a simpler prompt
- Reduce frames to 6

### Issue: Out of memory
**Solution:**
- Restart runtime
- Use fewer frames (6)
- Close other tabs

## 📊 Performance

| GPU | VRAM | Time | Quality |
|-----|------|------|---------|
| T4 | 16GB | 1-2 min | Good |
| V100 | 32GB | 1-1.5 min | Excellent |
| A100 | 40GB | 30-60 sec | Excellent |

## 🎯 Tips for Better Results

### 1. Keep Prompts Simple
✅ "A sunset over the ocean"
❌ "A cinematic sunset over the Pacific Ocean with golden waves..."

### 2. Use Fewer Frames
- 6-8 frames for very short videos
- 8-10 frames for short videos
- 10-12 frames for longer shorts

### 3. Use Fewer Steps
- 10-12 steps for speed
- 15-18 steps for balance (recommended)
- 20 steps for quality

### 4. Optimal Settings
```
Frames: 8
Steps: 15
Guidance: 7.5
FPS: 8
Duration: ~1 second
```

## 📱 Perfect For

- ✅ YouTube Shorts (9:16 aspect ratio)
- ✅ Facebook Reels
- ✅ Instagram Reels
- ✅ TikTok videos
- ✅ WhatsApp Status
- ✅ Snapchat Stories

## 🔗 Links

- **GitHub**: https://github.com/Vikram-Bosak/ltx-video-generator
- **Notebook**: https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Short_Video_Generator.ipynb
- **Full Version**: Text_to_Video_Generator_Fixed.ipynb (for longer videos)

## 💬 Need Help?

If you have issues:
1. Check the troubleshooting section above
2. Try with default settings first
3. Use simple prompts
4. Make sure GPU is enabled

---

**Made for quick, easy short video generation!** 🎬
