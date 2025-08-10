import os
from pathlib import Path

# 创建目录结构
def create_directory_structure(base_dir):
    dirs = [
        "css",
        "js",
        "images",
        "posts"  # 空文章目录
    ]
    
    for dir_name in dirs:
        os.makedirs(os.path.join(base_dir, dir_name), exist_ok=True)

# 创建HTML文件
def create_html_files(base_dir):
    # 首页HTML
    index_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTPS-CDY的博客</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="icon.ico" type="image/x-icon">
</head>
<body>
    <header>
        <div class="logo-container">
            <img src="HTPS logo.png" alt="HTPS Logo" class="logo">
            <h1>HTPS-CDY的博客</h1>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">首页</a></li>
                <li><a href="about.html">关于</a></li>
                <li><a href="contact.html">联系</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="welcome">
            <h2>欢迎来到我的博客</h2>
            <p>这里将分享我的技术学习和生活感悟。</p>
        </section>
        
        <section class="posts">
            <h2>文章列表</h2>
            <div class="post-list" id="postList">
                <!-- 文章将通过JavaScript动态加载 -->
                <p>暂无文章</p>
            </div>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 HTPS-CDY. 保留所有权利。</p>
    </footer>
    
    <script src="js/main.js"></script>
</body>
</html>"""
    
    # 关于页面HTML
    about_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>关于 - HTPS-CDY的博客</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="icon.ico" type="image/x-icon">
</head>
<body>
    <header>
        <div class="logo-container">
            <img src="HTPS logo.png" alt="HTPS Logo" class="logo">
            <h1>HTPS-CDY的博客</h1>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">首页</a></li>
                <li><a href="about.html">关于</a></li>
                <li><a href="contact.html">联系</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="about">
            <h2>关于我</h2>
            <p>你好，我是HTPS-CDY，一名技术爱好者。</p>
            <p>这个博客是我分享学习和思考的地方。</p>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 HTPS-CDY. 保留所有权利。</p>
    </footer>
</body>
</html>"""
    
    # 联系页面HTML
    contact_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>联系 - HTPS-CDY的博客</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="icon" href="icon.ico" type="image/x-icon">
</head>
<body>
    <header>
        <div class="logo-container">
            <img src="HTPS logo.png" alt="HTPS Logo" class="logo">
            <h1>HTPS-CDY的博客</h1>
        </div>
        <nav>
            <ul>
                <li><a href="index.html">首页</a></li>
                <li><a href="about.html">关于</a></li>
                <li><a href="contact.html">联系</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <section class="contact">
            <h2>联系我</h2>
            <form id="contactForm">
                <div class="form-group">
                    <label for="name">姓名:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">邮箱:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="message">留言:</label>
                    <textarea id="message" name="message" rows="5" required></textarea>
                </div>
                <button type="submit">发送</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 HTPS-CDY. 保留所有权利。</p>
    </footer>
    
    <script src="js/contact.js"></script>
</body>
</html>"""
    
    # 写入HTML文件
    with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    
    with open(os.path.join(base_dir, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_html)
    
    with open(os.path.join(base_dir, "contact.html"), "w", encoding="utf-8") as f:
        f.write(contact_html)

# 创建CSS文件
def create_css_files(base_dir):
    css_content = """/* 全局样式 */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Arial', sans-serif;
}

body {
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* 头部样式 */
header {
    background-color: #2c3e50;
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.logo-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
}

.logo {
    height: 50px;
    margin-right: 15px;
}

header h1 {
    font-size: 2rem;
}

nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
    transition: color 0.3s;
}

nav ul li a:hover {
    color: #3498db;
}

/* 主体内容样式 */
main {
    max-width: 1200px;
    margin: 2rem auto;
    padding: 0 20px;
}

section {
    margin-bottom: 2rem;
    padding: 20px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
    color: #2c3e50;
    margin-bottom: 1rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #3498db;
}

/* 文章列表样式 */
.post-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.post-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.post-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.post-card h3 {
    color: #2c3e50;
    margin-bottom: 0.5rem;
}

.post-card p {
    color: #666;
    font-size: 0.9rem;
}

/* 联系表单样式 */
form {
    max-width: 600px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 1rem;
}

label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
}

input, textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
}

textarea {
    resize: vertical;
    min-height: 100px;
}

button {
    background-color: #3498db;
    color: white;
    border: none;
    padding: 0.7rem 1.5rem;
    font-size: 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #2980b9;
}

/* 页脚样式 */
footer {
    text-align: center;
    padding: 1rem 0;
    background-color: #2c3e50;
    color: white;
    margin-top: 2rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
    .logo-container {
        flex-direction: column;
        text-align: center;
    }
    
    .logo {
        margin-right: 0;
        margin-bottom: 10px;
    }
    
    nav ul {
        flex-direction: column;
        align-items: center;
    }
    
    nav ul li {
        margin: 5px 0;
    }
}"""
    
    with open(os.path.join(base_dir, "css", "style.css"), "w", encoding="utf-8") as f:
        f.write(css_content)

# 创建JavaScript文件
def create_js_files(base_dir):
    # 主JS文件
    main_js = """// 动态加载文章列表
document.addEventListener('DOMContentLoaded', function() {
    // 这里可以添加从服务器获取文章列表的逻辑
    // 目前留空，因为博客中没有文章
});"""
    
    # 联系表单JS
    contact_js = """// 联系表单处理
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // 获取表单数据
            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };
            
            // 这里可以添加表单提交逻辑
            console.log('表单已提交:', formData);
            
            // 显示成功消息
            alert('感谢您的留言！我会尽快回复您。');
            
            // 重置表单
            contactForm.reset();
        });
    }
});"""
    
    with open(os.path.join(base_dir, "js", "main.js"), "w", encoding="utf-8") as f:
        f.write(main_js)
    
    with open(os.path.join(base_dir, "js", "contact.js"), "w", encoding="utf-8") as f:
        f.write(contact_js)

# 创建README文件
def create_readme(base_dir):
    readme_content = """# HTPS-CDY 博客

这是一个简单的静态博客网站，使用HTML、CSS和JavaScript构建。

## 项目结构

- `index.html`: 博客首页
- `about.html`: 关于页面
- `contact.html`: 联系页面
- `css/`: 样式表目录
  - `style.css`: 主样式表
- `js/`: JavaScript脚本目录
  - `main.js`: 主脚本
  - `contact.js`: 联系表单脚本
- `images/`: 图片资源目录
- `posts/`: 文章目录（当前为空）

## 部署说明

1. 将整个项目上传到GitHub仓库
2. 启用GitHub Pages功能

## 使用说明

1. 在`posts/`目录中添加HTML格式的文章
2. 修改`js/main.js`来动态加载文章列表
3. 自定义样式可以在`css/style.css`中修改

## 注意事项

- 当前博客没有后端功能，联系表单仅做前端演示
- 如需完整功能，需要添加后端处理逻辑"""
    
    with open(os.path.join(base_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

def main():
    # 设置基础目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("正在创建博客网站结构...")
    
    # 创建目录结构
    create_directory_structure(base_dir)
    
    # 创建HTML文件
    create_html_files(base_dir)
    
    # 创建CSS文件
    create_css_files(base_dir)
    
    # 创建JavaScript文件
    create_js_files(base_dir)
    
    # 创建README文件
    create_readme(base_dir)
    
    print("博客网站结构创建完成！")
    print(f"请将 icon.ico 和 HTPS logo.png 放入 {base_dir} 目录")
    print("然后可以将整个项目上传到GitHub仓库并启用GitHub Pages")

if __name__ == "__main__":
    main()