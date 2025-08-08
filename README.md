# 💻 Laptop Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link-here.streamlit.app)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A smart web application that predicts laptop prices using machine learning based on hardware specifications and features.


## 🌟 Overview

The **Laptop Price Predictor** is an intelligent web application built with Streamlit that helps users estimate laptop prices based on various hardware specifications. Whether you're a consumer looking to budget for your next laptop purchase, a retailer setting competitive prices, or a market researcher analyzing pricing trends, this tool provides data-driven price predictions in real-time.

### ✨ Key Features

- 🎯 **Accurate Price Predictions** - ML-powered price estimation based on 12+ hardware specifications
- 🖥️ **Interactive Web Interface** - User-friendly form-based input with real-time results
- 📱 **Responsive Design** - Works seamlessly across desktop and mobile devices
- ⚡ **Real-time Processing** - Instant price predictions without page reloads
- 🔧 **Comprehensive Inputs** - Covers all major laptop specifications (CPU, RAM, GPU, storage, display, etc.)
- 📊 **Smart Feature Engineering** - Calculates derived metrics like PPI for enhanced accuracy


## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.7+
- **Machine Learning**: Scikit-learn
- **Data Processing**: NumPy, Pandas
- **Model Serialization**: Pickle

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher installed
- pip package manager
- At least 512MB of available RAM

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/UzmaMasroor/Laptop-Price-Prediction
cd laptop-price-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

### 4. Open in Browser

The application will automatically open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
laptop-price-predictor/
│
├── app.py                 # Main Streamlit application
├── pipe.pkl              # Pre-trained ML model pipeline
├── df.pkl                # Reference dataset for dropdown options
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── screenshots/         # Application screenshots
```

## 🎮 How to Use

1. **Launch the Application** - Run the Streamlit app using the command above
2. **Enter Laptop Specifications**:
   - Select brand, type, and processor
   - Choose RAM, storage options (HDD/SSD)
   - Specify display characteristics (size, resolution, touchscreen)
   - Set additional features (weight, graphics card, OS)
3. **Get Instant Prediction** - Click "Predict Price" to get your estimate
4. **Analyze Results** - Review the predicted price and adjust specifications as needed

## 🔧 Input Parameters

| Parameter | Type | Description | Example Values |
|-----------|------|-------------|----------------|
| **Company** | Dropdown | Laptop brand/manufacturer | Apple, Dell, HP, Lenovo |
| **Type** | Dropdown | Laptop category | Ultrabook, Gaming, Business |
| **RAM** | Dropdown | System memory in GB | 4, 8, 16, 32 GB |
| **Weight** | Slider | Physical weight in kg | 1.2 - 3.5 kg |
| **CPU** | Dropdown | Processor brand | Intel Core i5, AMD Ryzen 7 |
| **Touchscreen** | Radio | Touch capability | Yes/No |
| **IPS Display** | Radio | Display technology | Yes/No |
| **Screen Size** | Slider | Display diagonal in inches | 11.6" - 17.3" |
| **Resolution** | Dropdown | Display resolution | 1920x1080, 2560x1440 |
| **GPU** | Dropdown | Graphics processor | Intel Integrated, NVIDIA GTX |
| **HDD** | Dropdown | Hard disk storage in GB | 0, 500, 1000 GB |
| **SSD** | Dropdown | Solid state storage in GB | 128, 256, 512, 1024 GB |
| **OS** | Dropdown | Operating system | Windows 10, macOS, Linux |

## 🤖 Machine Learning Pipeline

The application uses a sophisticated ML pipeline that includes:

- **Feature Engineering**: Automatic calculation of PPI (Pixels Per Inch) from resolution and screen size
- **Categorical Encoding**: Proper handling of brand names and specifications
- **Binary Transformation**: Yes/No inputs converted to numerical format
- **Logarithmic Scaling**: Model trained on log-transformed prices for better accuracy
- **Exponential Output**: Final predictions converted back to actual price range

## 📊 Model Performance

- **Training Data**: Comprehensive dataset of laptop specifications and prices
- **Feature Count**: 12+ engineered features for optimal prediction accuracy
- **Output Range**: Predicts prices across various laptop segments
- **Validation**: Cross-validated for consistent performance

## 🚀 Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Streamlit Cloud
1. Fork this repository
2. Connect your GitHub account to Streamlit Cloud
3. Deploy directly from your repository

### Heroku
```bash
# Create Procfile with: web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make Your Changes**
4. **Commit Your Changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
5. **Push to the Branch**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### 🐛 Bug Reports

Found a bug? Please open an issue with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### 💡 Feature Requests

Have an idea? We'd love to hear it! Open an issue with:
- Feature description
- Use case/motivation
- Possible implementation approach

## 🔮 Future Enhancements

- [ ] **Price Range Predictions** - Add confidence intervals
- [ ] **Comparison Tool** - Side-by-side laptop comparison
- [ ] **Historical Trends** - Price trend analysis over time
- [ ] **Export Functionality** - PDF/CSV report generation
- [ ] **Mobile App** - React Native or Flutter implementation
- [ ] **API Endpoint** - RESTful API for third-party integrations
- [ ] **Advanced Filters** - More granular specification options
- [ ] **Dark Mode** - Theme switching capability

## 📈 Performance & Scaling

- **Response Time**: < 2 seconds for price predictions
- **Concurrent Users**: Optimized for multiple simultaneous users
- **Memory Usage**: Efficient model loading and caching
- **Scalability**: Cloud-ready architecture

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit Team** - For the amazing web app framework
- **Scikit-learn Community** - For robust machine learning tools
- **Open Source Contributors** - For inspiration and code examples

## 📞 Contact & Support

- **Author**: [Uzma Masroor](https://github.com/UzmaMasroor/Laptop-Price-Prediction)
- **Email**: uzmaa.masroor@gmail.com
- **LinkedIn**: [Uzma Masroor](https://www.linkedin.com/in/uzma-masroor-/)
- **Project Issues**: [GitHub Issues](https://github.com/UzmaMasroor/Laptop-Price-Prediction)

## ⭐ Show Your Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking for your own experiments
- 🐛 Reporting issues or suggesting improvements
- 📢 Sharing with others who might find it useful

---

<p align="center">
  <strong>Made with ❤️ and Python</strong>
</p>

<p align="center">
  <a href="https://streamlit.io" target="_blank">
    <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Powered by Streamlit" width="50">
  </a>
</p>
