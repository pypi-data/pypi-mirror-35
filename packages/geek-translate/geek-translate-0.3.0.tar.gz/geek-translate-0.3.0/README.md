## **搜狗翻译API**


### **基本使用**
1. 调用搜狗翻译API，需要传3个参数text,target,from_target
2. text为要翻译的文本（必传，type可以是str或者list）
3. target为要翻译成的语言（可不传，默认为'en'，英文）
4. from_target为传入的text的语言（可不传，默认为'zh-CHS'，中文）

### **相关说明**
#### **接口地址**
http://snapshot.sogoucdn.com/engtranslate
#### **请求方式**
只支持POST请求
#### **请求数据和返回数据格式**
JSON对象