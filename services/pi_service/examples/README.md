# 📁 Examples - PII De-identification Service

This folder contains comprehensive examples demonstrating how to use the modular PII de-identification system with different types of data and use cases.

## 🎯 **What's Included**

### 📊 **Sample Data**
- `data/sample_ticket.json` - Customer support ticket with conversations
- `data/sample_emails.json` - Business email communications
- `data/sample_texts.json` - Various text types (support, medical, employment, financial)

### 🔧 **Example Scripts**

#### 1. **Basic Usage** (`basic_usage.py`)
**Perfect for beginners!**
- Shows the simplest way to anonymize text
- Single text processing
- Step-by-step explanation
- No file I/O complexity

```bash
python examples/basic_usage.py
```

#### 2. **Intermediate Usage** (`intermediate_usage.py`)
**Great for processing files!**
- Processes different data file types
- Saves anonymized results to files
- Shows how to handle structured data
- Demonstrates field-by-field anonymization

```bash
python examples/intermediate_usage.py
```

#### 3. **Advanced Usage** (`advanced_usage.py`)
**Production-ready features!**
- Custom pipeline configuration
- Batch processing with monitoring
- Performance tracking
- Comprehensive error handling

```bash
python examples/advanced_usage.py
```

## 📁 **Output Structure**

After running the examples, you'll find anonymized results in:
```
examples/outputs/
├── anonymized_texts.json      # Basic text processing results
├── anonymized_emails.json     # Email processing results
├── anonymized_ticket.json     # Ticket processing results
├── batch_anonymized_texts.json # Advanced batch processing
├── batch_anonymized_emails.json
└── batch_anonymized_ticket.json
```

## 🚀 **Getting Started**

### **For Beginners:**
1. Start with `basic_usage.py` to understand the core concepts
2. Look at the sample data in `data/` folder
3. Run the example and see the output

### **For File Processing:**
1. Run `intermediate_usage.py` to process different file types
2. Check the `outputs/` folder for results
3. Compare original vs anonymized data

### **For Production Use:**
1. Run `advanced_usage.py` to see monitoring and batch processing
2. Study the custom pipeline configuration
3. Use the monitoring features for performance tracking

## 📊 **Sample Data Overview**

### **Ticket Data** (`sample_ticket.json`)
- Customer support ticket with personal information
- Nested conversation structure
- Multiple PII types (names, emails, phones, addresses)

### **Email Data** (`sample_emails.json`)
- Business email communications
- Medical, client, and financial information
- Various PII patterns and formats

### **Text Data** (`sample_texts.json`)
- Support conversations
- Medical reports
- Job applications
- Financial documents

## 🔍 **What You'll Learn**

### **From Basic Usage:**
- How to load pipeline configuration
- How to build and use a pipeline
- Simple text anonymization
- Error handling basics

### **From Intermediate Usage:**
- File I/O operations
- Structured data processing
- Field-specific anonymization
- Result saving and organization

### **From Advanced Usage:**
- Custom pipeline configuration
- Batch processing techniques
- Performance monitoring
- Production-ready patterns

## 💡 **Tips for Using Examples**

1. **Start Simple**: Begin with `basic_usage.py` even if you're experienced
2. **Check Data**: Look at the sample data files to understand the structure
3. **Compare Results**: Always compare original vs anonymized output
4. **Modify Data**: Try changing the sample data to test different scenarios
5. **Customize Configs**: Modify pipeline configurations in `advanced_usage.py`

## 🎯 **Next Steps**

After running the examples:

1. **Try Your Own Data**: Replace sample data with your own files
2. **Customize Pipelines**: Modify configurations for your specific needs
3. **Add Monitoring**: Use the monitoring features for production
4. **Extend Functionality**: Add new recognizers or operators

## 📚 **Related Documentation**

- `../README.md` - Main project documentation
- `../PROJECT_STRUCTURE.md` - Project structure overview
- `../user_interface.py` - Interactive user interface

---

**🎉 These examples will help you understand and use the modular PII de-identification system effectively!** 