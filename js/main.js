document.addEventListener('DOMContentLoaded', function() {
    // 文章数据
    const articles = [
        {
            title: "实验",
            date: "2025-08-10",
            description: "一篇包含图片的实验性文章",
            image: "./images/2.png",
            url: "./posts/experiment.html"
        }
    ];

    const postList = document.getElementById('postList');
    
    if (!articles.length) {
        postList.innerHTML = '<p>暂无文章</p>';
        return;
    }

    postList.innerHTML = ''; // 清空默认内容

    articles.forEach(article => {
        const articleCard = document.createElement('div');
        articleCard.className = 'post-card';
        articleCard.innerHTML = `
            <a href="${article.url}" class="post-link">
                ${article.image ? `<img src="${article.image}" alt="${article.title}" class="post-thumbnail">` : ''}
                <div class="post-content">
                    <h3>${article.title}</h3>
                    <time datetime="${article.date}">${formatDate(article.date)}</time>
                    <p>${article.description}</p>
                </div>
            </a>
        `;
        postList.appendChild(articleCard);
    });

    // 日期格式化
    function formatDate(dateString) {
        const date = new Date(dateString);
        return `${date.getFullYear()}年${date.getMonth()+1}月${date.getDate()}日`;
    }
});
