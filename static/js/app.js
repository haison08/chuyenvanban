document.addEventListener('DOMContentLoaded', () => {
  // DOM Elements
  const dropZone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');
  const dropContent = document.getElementById('dropContent');
  const filePreviewBar = document.getElementById('filePreviewBar');
  const fileName = document.getElementById('fileName');
  const fileMeta = document.getElementById('fileMeta');
  const removeFileBtn = document.getElementById('removeFileBtn');
  const browseBtn = document.getElementById('browseBtn');
  const demoBtn = document.getElementById('demoBtn');
  
  const optionsToggle = document.getElementById('optionsToggle');
  const optionsContainer = document.querySelector('.options-container');
  const removeSignatures = document.getElementById('removeSignatures');
  const autoLandscape = document.getElementById('autoLandscape');
  const fontSelect = document.getElementById('fontSelect');
  const apiKeyInput = document.getElementById('apiKeyInput');
  
  const convertBtn = document.getElementById('convertBtn');
  const progressCard = document.getElementById('progressCard');
  const progressStatusText = document.getElementById('progressStatusText');
  const progressFill = document.getElementById('progressFill');
  const stepItems = [
    document.getElementById('step1'),
    document.getElementById('step2'),
    document.getElementById('step3'),
    document.getElementById('step4')
  ];
  
  const errorCard = document.getElementById('errorCard');
  const errorTitle = document.getElementById('errorTitle');
  const errorDesc = document.getElementById('errorDesc');
  const retryBtn = document.getElementById('retryBtn');
  
  const resultCard = document.getElementById('resultCard');
  const resultFilename = document.getElementById('resultFilename');
  const resultSubtitle = document.getElementById('resultSubtitle');
  const downloadBtn = document.getElementById('downloadBtn');
  const resetBtn = document.getElementById('resetBtn');
  
  let currentFile = null;
  
  const savedApiKey = localStorage.getItem('documorph_api_key') || '';
  if (savedApiKey) {
    apiKeyInput.value = savedApiKey;
  }
  
  apiKeyInput.addEventListener('input', () => {
    localStorage.setItem('documorph_api_key', apiKeyInput.value.trim());
  });

  // Toggle Options Accordion
  optionsToggle.addEventListener('click', () => {
    optionsContainer.classList.toggle('open');
  });

  // Browse File Button
  browseBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    fileInput.click();
  });

  dropZone.addEventListener('click', () => {
    if (!currentFile) {
      fileInput.click();
    }
  });

  // Drag & Drop
  ['dragenter', 'dragover'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropZone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropZone.classList.remove('dragover');
    });
  });

  dropZone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    const files = dt.files;
    if (files.length > 0) {
      handleSelectedFile(files[0]);
    }
  });

  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      handleSelectedFile(fileInput.files[0]);
    }
  });

  // Paste from clipboard support
  window.addEventListener('paste', (e) => {
    const items = (e.clipboardData || e.originalEvent.clipboardData).items;
    for (const item of items) {
      if (item.kind === 'file') {
        const file = item.getAsFile();
        handleSelectedFile(file);
        break;
      }
    }
  });

  function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
  }

  function handleSelectedFile(file) {
    const validExtensions = ['.pdf', '.png', '.jpg', '.jpeg', '.tiff', '.webp', '.bmp'];
    const ext = '.' + file.name.split('.').pop().toLowerCase();
    
    if (!validExtensions.includes(ext)) {
      alert('Vui lòng chọn file PDF hoặc file ảnh hợp lệ (PNG, JPG, JPEG, TIFF)!');
      return;
    }
    
    currentFile = file;
    fileName.textContent = file.name;
    fileMeta.textContent = `${formatBytes(file.size)} • ${file.type || 'Tài liệu'}`;
    
    dropContent.classList.add('hidden');
    filePreviewBar.classList.remove('hidden');
    convertBtn.disabled = false;
    
    // Hide previous results
    resultCard.classList.add('hidden');
  }

  removeFileBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    currentFile = null;
    fileInput.value = '';
    dropContent.classList.remove('hidden');
    filePreviewBar.classList.add('hidden');
    convertBtn.disabled = true;
  });

  // Convert Button Click
  convertBtn.addEventListener('click', async () => {
    if (!currentFile) return;
    
    startConversionProcess();
    
    const formData = new FormData();
    formData.append('file', currentFile);
    formData.append('apiKey', apiKeyInput.value.trim());
    formData.append('removeSignatures', removeSignatures.checked);
    formData.append('autoLandscape', autoLandscape.checked);
    formData.append('fontName', fontSelect.value);
    
    try {
      const response = await fetch('/api/convert', {
        method: 'POST',
        body: formData
      });
      
      const data = await response.json();
      
      if (!response.ok || !data.success) {
        throw new Error(data.message || 'Chuyển đổi thất bại');
      }
      
      finishConversionProcess(data);
    } catch (err) {
      progressCard.classList.add('hidden');
      errorCard.classList.remove('hidden');
      errorDesc.textContent = err.message;
      convertBtn.disabled = false;
    }
  });

  retryBtn.addEventListener('click', () => {
    errorCard.classList.add('hidden');
    convertBtn.click();
  });

  // Demo Button Click
  demoBtn.addEventListener('click', async (e) => {
    e.stopPropagation();
    
    currentFile = { name: "Tai_Lieu_Mau_Ke_Hoach_2026.pdf", size: 2670620, type: "application/pdf" };
    fileName.textContent = currentFile.name;
    fileMeta.textContent = "2.55 MB • Kế hoạch MTTQ 6 trang (Bao gồm bảng biểu phụ lục)";
    dropContent.classList.add('hidden');
    filePreviewBar.classList.remove('hidden');
    
    startConversionProcess();
    
    try {
      const response = await fetch('/api/demo', {
        method: 'POST'
      });
      
      const data = await response.json();
      
      if (!response.ok || !data.success) {
        throw new Error(data.message || 'Demo thất bại');
      }
      
      finishConversionProcess(data);
    } catch (err) {
      alert('Lỗi Demo: ' + err.message);
      progressCard.classList.add('hidden');
      convertBtn.disabled = false;
    }
  });

  function updateStep(index, statusText, percent) {
    progressStatusText.textContent = statusText;
    progressFill.style.width = percent + '%';
    
    stepItems.forEach((step, idx) => {
      step.classList.remove('active', 'completed');
      if (idx < index) {
        step.classList.add('completed');
      } else if (idx === index) {
        step.classList.add('active');
      }
    });
  }

  function startConversionProcess() {
    convertBtn.disabled = true;
    resultCard.classList.add('hidden');
    errorCard.classList.add('hidden');
    progressCard.classList.remove('hidden');
    
    // Smooth step animations
    updateStep(0, 'Đang đọc và kết xuất từng trang hình ảnh độ nét cao...', 25);
    
    setTimeout(() => {
      updateStep(1, 'AI Vision đang phân tích nhận diện thể thức, bảng biểu & font chữ...', 55);
    }, 1200);
    
    setTimeout(() => {
      updateStep(2, 'Đang lắp ráp định dạng tài liệu Word (.docx) & xoay khổ ngang...', 85);
    }, 2400);
  }

  function finishConversionProcess(data) {
    updateStep(3, 'Chuyển đổi hoàn tất 100%! Đã sẵn sàng.', 100);
    
    setTimeout(() => {
      progressCard.classList.add('hidden');
      resultCard.classList.remove('hidden');
      
      resultFilename.textContent = data.filename;
      resultSubtitle.textContent = `${data.page_count} trang • Soạn thảo 100% • Đúng thể thức văn bản`;
      downloadBtn.href = data.download_url;
      
      // Auto trigger scroll to result
      resultCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 600);
  }

  // Reset to convert another file
  resetBtn.addEventListener('click', () => {
    currentFile = null;
    fileInput.value = '';
    dropContent.classList.remove('hidden');
    filePreviewBar.classList.add('hidden');
    resultCard.classList.add('hidden');
    errorCard.classList.add('hidden');
    convertBtn.disabled = true;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});
