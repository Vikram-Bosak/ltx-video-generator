# Google Colab VPS - Complete Guide

## 🎯 What is This?

Transform Google Colab into a **FREE VPS** with:
- 🖥️ Full Linux Desktop (XFCE)
- 🌐 Remote Desktop Access (VNC)
- ⚡ 16 Hours CPU Daily
- 💾 Persistent Storage (Google Drive)
- 🎯 Complete VPS Control
- 🚀 No Disturbance - Your Private Workspace

## 🚀 Quick Start

### Step 1: Get ngrok Token
1. Go to https://dashboard.ngrok.com/signup
2. Sign up for free account
3. Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
4. Copy the token (looks like: `2x...`)

### Step 2: Open Notebook
```
https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Google_Colab_VPS.ipynb
```

### Step 3: Setup VPS
1. Open the notebook
2. Find the cell with `NGROK_TOKEN = "YOUR_NGROK_TOKEN"`
3. Replace `YOUR_NGROK_TOKEN` with your actual token
4. Run all cells (Runtime → Run all)
5. Wait 2-3 minutes for setup
6. Click the VNC URL that appears
7. Enter password: `colab123` (or change it)

### Step 4: Enjoy Your VPS!
- You now have a full Linux desktop
- Access it from anywhere
- Use it like a real VPS
- All for FREE!

## ✨ Features

### 🖥️ Desktop Environment
- **XFCE Desktop** - Lightweight and fast
- **1280x720 Resolution** - Good for most tasks
- **Full Linux Terminal** - Complete command line access
- **File Manager** - Graphical file management
- **Web Browser** - Firefox pre-installed

### 🌐 Remote Access
- **VNC Server** - Remote desktop protocol
- **noVNC Web Client** - Browser-based access
- **ngrok Tunnel** - Secure remote access
- **Password Protected** - Secure connection

### 💾 Storage
- **Google Drive Integration** - Persistent storage
- **12-24 GB RAM** - Plenty of memory
- **100+ GB Disk Space** - Ample storage
- **File Upload/Download** - Easy file transfer

### ⚡ Performance
- **16 Hours CPU Daily** - Free compute time
- **Multi-core CPU** - Fast processing
- **High-speed Network** - Fast downloads
- **GPU Access** - Available for ML tasks

## 📋 What You Can Do

### Development
- ✅ Install Python, Node.js, PHP, etc.
- ✅ Run code and scripts
- ✅ Use Git for version control
- ✅ Install IDEs (VS Code, etc.)
- ✅ Develop web applications
- ✅ Test software

### Media
- ✅ Download and upload files
- ✅ Convert videos/images
- ✅ Run media processing tools
- ✅ Use FFmpeg for video editing
- ✅ Edit images with GIMP

### Web
- ✅ Host websites
- ✅ Run web servers
- ✅ Test web applications
- ✅ Use browser for development
- ✅ Run Node.js apps

### Automation
- ✅ Run cron jobs
- ✅ Schedule tasks
- ✅ Automate workflows
- ✅ Run bots and scripts
- ✅ Process data

### Storage
- ✅ Use Google Drive for persistence
- ✅ Upload/download files
- ✅ Manage file system
- ✅ Use cloud storage
- ✅ Backup files

## 🔧 Setup Instructions

### 1. Install ngrok Token

**Why needed?**
ngrok creates a secure tunnel to access your VPS from anywhere.

**How to get:**
1. Go to https://dashboard.ngrok.com/signup
2. Sign up (free)
3. Go to https://dashboard.ngrok.com/get-started/your-authtoken
4. Copy your authtoken

**How to use:**
In the notebook, find this line:
```python
NGROK_TOKEN = "YOUR_NGROK_TOKEN"
```

Replace `YOUR_NGROK_TOKEN` with your actual token:
```python
NGROK_TOKEN = "2xYzAbCdEfGhIjKlMnOpQrStUvWxYz"
```

### 2. Change VNC Password (Optional)

**Default password:** `colab123`

**How to change:**
In the notebook, find this line:
```python
VNC_PASSWORD = "colab123"
```

Replace with your desired password:
```python
VNC_PASSWORD = "your_secure_password"
```

### 3. Connect Google Drive (Optional)

**Why needed?**
Files in `/content` are deleted when session ends. Google Drive provides persistent storage.

**How to use:**
Run the "Connect Google Drive" cell. Your Drive will be mounted at:
```
/content/drive/MyDrive/colab_vps
```

**Best practices:**
- Save important files to Google Drive
- Use `/content/drive/MyDrive/colab_vps` for persistent storage
- Backup your work regularly

## 🔄 How to Reconnect

### If Session Disconnects:

1. **Open notebook again**
   - Go to: https://colab.research.google.com/github/Vikram-Bosak/ltx-video-generator/blob/main/Google_Colab_VPS.ipynb

2. **Run all cells**
   - Runtime → Run all
   - Wait 2-3 minutes

3. **Get new VNC URL**
   - The ngrok cell will display a new URL
   - Use this URL to connect

4. **Access your desktop**
   - Click the VNC URL
   - Enter your password
   - Your desktop is back!

### What's Lost:
- Files in `/content` (not in Google Drive)
- Running processes
- Open applications

### What's Preserved:
- Files in Google Drive
- Installed software (need to reinstall)
- Your settings

## 🛠️ Useful Commands

### System Commands

```bash
# Check running processes
ps aux

# Check system resources
htop

# Check disk space
df -h

# Check memory
free -h

# Kill a process
kill <PID>

# Install software
apt-get install <package>

# Update system
apt-get update && apt-get upgrade
```

### File Management

```bash
# Navigate to Google Drive
cd /content/drive/MyDrive/colab_vps

# List files
ls -la

# Create directory
mkdir myfolder

# Copy file to Drive
cp /content/myfile.txt /content/drive/MyDrive/colab_vps/

# Move file
mv file.txt newlocation/

# Delete file
rm file.txt

# Download file
wget https://example.com/file.zip

# Extract zip
unzip file.zip
```

### Python

```bash
# Run Python script
python3 script.py

# Install Python package
pip3 install package_name

# Create virtual environment
python3 -m venv myenv
source myenv/bin/activate
```

### Node.js

```bash
# Run Node.js app
node app.js

# Install npm package
npm install package_name

# Run npm script
npm run start
```

### Git

```bash
# Clone repository
git clone https://github.com/user/repo.git

# Pull changes
git pull

# Push changes
git push

# Check status
git status
```

## 📊 Performance Tips

### For Better Performance:

1. **Use Lightweight Apps**
   - XFCE is already lightweight
   - Avoid heavy applications
   - Use terminal when possible

2. **Monitor Resources**
   - Use `htop` to monitor CPU/RAM
   - Close unused applications
   - Restart if system is slow

3. **Optimize Storage**
   - Clean temporary files regularly
   - Use Google Drive for large files
   - Delete unnecessary files

4. **Network Optimization**
   - Use wget for downloads
   - Compress files before transfer
   - Use efficient protocols

## ⚠️ Important Notes

### Limitations:

1. **Session Time**
   - Standard: 12 hours
   - Pro: 24 hours
   - After timeout, session disconnects

2. **Storage**
   - `/content` is temporary
   - Files deleted after session
   - Use Google Drive for persistence

3. **Network**
   - Some ports may be blocked
   - External access limited
   - Use ngrok for remote access

4. **GPU**
   - GPU access is limited
   - Not always available
   - May require Colab Pro

### Best Practices:

1. **Save Work Regularly**
   - Save to Google Drive
   - Backup important files
   - Use version control

2. **Keep Notebook Running**
   - Don't close the tab
   - Keep Colab tab open
   - Monitor connection

3. **Use Efficient Tools**
   - Lightweight applications
   - Command line tools
   - Optimized workflows

4. **Security**
   - Change default password
   - Don't share ngrok URL
   - Use strong passwords
   - Be careful with downloads

## 🔒 Security Tips

### Protect Your VPS:

1. **Change Default Password**
   ```python
   VNC_PASSWORD = "your_strong_password"
   ```

2. **Don't Share ngrok URL**
   - Keep it private
   - Regenerate if compromised
   - Use authentication

3. **Use Strong Passwords**
   - Mix letters, numbers, symbols
   - At least 12 characters
   - Don't reuse passwords

4. **Be Careful with Downloads**
   - Only download from trusted sources
   - Scan files before opening
   - Don't run unknown scripts

5. **Keep Software Updated**
   ```bash
   apt-get update && apt-get upgrade
   ```

## 🎯 Use Cases

### 1. Development Server
- Host development websites
- Test applications
- Run development databases
- Collaborate with team

### 2. Media Processing
- Convert videos
- Edit images
- Process audio
- Render graphics

### 3. Automation
- Run scheduled tasks
- Process data
- Automate workflows
- Run bots

### 4. Learning
- Practice Linux commands
- Learn system administration
- Experiment with software
- Test configurations

### 5. Temporary Workspace
- Quick testing
- Prototyping
- Demo environments
- Temporary projects

## 🆘 Troubleshooting

### Issue: VNC Not Connecting

**Solution:**
1. Make sure ngrok is running
2. Check if VNC server is started
3. Verify ngrok token is correct
4. Try restarting the notebook

### Issue: Desktop is Slow

**Solution:**
1. Close unused applications
2. Check system resources with `htop`
3. Restart the notebook
4. Use fewer applications

### Issue: Files Not Saving

**Solution:**
1. Save to Google Drive
2. Check Drive is mounted
3. Verify file path
4. Use persistent storage

### Issue: Session Disconnected

**Solution:**
1. Reopen the notebook
2. Run all cells again
3. Get new VNC URL
4. Reconnect to desktop

### Issue: Software Not Installing

**Solution:**
1. Update package list: `apt-get update`
2. Check package name is correct
3. Try alternative package
4. Check for errors

## 📚 Additional Resources

### Documentation:
- [Google Colab Documentation](https://colab.research.google.com/)
- [ngrok Documentation](https://ngrok.com/docs)
- [XFCE Documentation](https://docs.xfce.org/)

### Tutorials:
- [Linux Command Line](https://linuxjourney.com/)
- [VNC Setup](https://www.realvnc.com/en/connect/)
- [Google Drive API](https://developers.google.com/drive)

### Communities:
- [Google Colab Community](https://stackoverflow.com/questions/tagged/google-colaboratory)
- [Linux Forums](https://www.linux.org/forums/)
- [ngrok Community](https://ngrok.com/community)

## 🎉 Conclusion

You now have a **FREE VPS** with:
- ✅ Full Linux desktop
- ✅ Remote access
- ✅ 16 hours CPU daily
- ✅ Persistent storage
- ✅ Complete control

**Enjoy your free VPS!** 🚀

---

**Need Help?**
- Check the troubleshooting section
- Review the documentation
- Ask in communities
- Experiment and learn!

**Remember:**
- Keep notebook running
- Save to Google Drive
- Change default password
- Have fun exploring!
