# Research Publication Search Engine + Document Classification

**Coventry University - Information Retrieval Assignment**  
**Student**: Rishesh Shrestha  
**Module**: ST7071CEM - Intelligent Information Retrieval

---

## 🚀 Quick Start

### Run Everything with One Command:
```bash
python run_project.py
```

This will:
- ✅ Start Django backend (http://127.0.0.1:8000)
- ✅ Start React frontend (http://localhost:5173)
- ✅ Open browser automatically

**Stop servers**: Press `Ctrl+C`

---

## 📋 Project Overview

This project implements two main tasks:

### Task 1: Vertical Search Engine
- Web crawler for Coventry University research publications
- Inverted index construction
- Query processor with relevance ranking
- **Access**: http://localhost:5173/

### Task 2: Document Classification
- Multinomial Naïve Bayes classifier
- TF-IDF feature extraction
- Three categories: Business, Entertainment, Health
- **Access**: http://localhost:5173/classification

---

## 📂 Project Structure

```
final task/
├── backend/                    # Django backend
│   ├── classification/         # Task 2: Document classification
│   ├── search_engine/          # Task 1: Search engine
│   ├── models/                 # Trained ML models
│   └── data/                   # Datasets and metrics
├── frontend/                   # React frontend
│   └── src/components/         # UI components
├── run_project.py              # 🎯 Main launcher (run this!)
├── run_task2_classification.py # Train classification model
├── generate_dataset.py         # Generate training data
└── TASK2_*.md                  # Documentation files
```

---

## 🎯 Available Pages

| Page | URL | Description |
|------|-----|-------------|
| Search Engine | http://localhost:5173/ | Search research publications |
| Classification | http://localhost:5173/classification | Classify documents |
| Statistics | http://localhost:5173/stats | View clustering statistics |
| Crawler | http://localhost:5173/crawl | Web crawler interface |

---

## 📊 Task 2 Model Performance

- **Accuracy**: 90% (on real-world news data)
- **Categories**: Business, Entertainment, Health
- **Dataset**: 150 real-world articles from BBC News & The Guardian
- **Distribution**: 50 documents per category
- **Algorithm**: Multinomial Naïve Bayes
- **Features**: TF-IDF with bigrams

### Per-Category Performance
| Category | Precision | Recall | F1-Score |
|----------|-----------|--------|----------|
| Business | 100% | 70% | 82% |
| Entertainment | 91% | 100% | 95% |
| Health | 83% | 100% | 91% |

---

## 🔧 Manual Setup (if needed)

### 1. Install Dependencies
```bash
# Backend
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

### 2. Train Classification Model
```bash
python run_task2_classification.py
```

### 3. Run Servers Separately
```bash
# Terminal 1 - Backend
cd backend
python manage.py runserver

# Terminal 2 - Frontend
cd frontend
npm run dev
```

---

## 📖 Documentation

- **TASK2_SUMMARY.md** - Complete implementation overview
- **TASK2_DOCUMENTATION.md** - Technical documentation
- **TASK2_QUICK_REFERENCE.md** - Quick commands and tips
- **TASK2_ARCHITECTURE.md** - System architecture diagrams

---

## ✅ Assignment Requirements

### Task 1: Search Engine
- ✅ Web crawler (BFS, robots.txt compliant)
- ✅ Inverted index construction
- ✅ Query processor with ranking
- ✅ Web interface

### Task 2: Document Classification
- ✅ 120 labeled documents (3 categories)
- ✅ Multinomial Naïve Bayes classifier
- ✅ TF-IDF features with preprocessing
- ✅ Model evaluation (accuracy, precision, recall, F1)
- ✅ Robustness testing (varied inputs)
- ✅ Web interface for predictions
- ✅ API endpoints

---

## 🧪 Testing

### Test Classification API
```bash
python test_classification_api.py
```

### Example Predictions
- "The central bank increased interest rates" → **Business**
- "The actor won an award for his movie" → **Entertainment**
- "Doctors warn about rising flu cases" → **Health**

---

## 🎓 For Report/Viva

### Screenshots to Take:
1. Training output from `run_task2_classification.py`
2. Web interface showing predictions
3. API responses with confidence scores
4. Search engine results
5. Crawler in action

### Key Points to Explain:
- Why Multinomial Naïve Bayes for text classification
- How TF-IDF works and why bigrams are used
- Preprocessing pipeline
- Model evaluation metrics
- Robustness testing results

---

## 💡 Tips

- **First time running?** Just use `python run_project.py`
- **Model not found?** Run `python run_task2_classification.py` first
- **Port conflicts?** Check if ports 8000 or 5173 are already in use
- **Need help?** Check the TASK2_*.md documentation files

---

## 📞 Support

If you encounter issues:
1. **Check TROUBLESHOOTING.md** for common issues and solutions
2. Ensure Python dependencies are installed: `pip install -r backend/requirements.txt`
3. Ensure Node dependencies are installed: `cmd /c npm install` (in frontend/)
4. Check that ports 8000 and 5173 are available
5. Review documentation files for detailed instructions

**PowerShell Issues?** The script now uses `cmd /c npm` to avoid execution policy errors.

---

**Status**: ✅ Complete and Ready for Submission  
**Last Updated**: 2026-01-22
