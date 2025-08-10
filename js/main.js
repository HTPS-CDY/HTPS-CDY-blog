document.addEventListener('DOMContentLoaded', function() {
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

    postList.innerHTML = '';

    articles.forEach(article => {
        const articleCard = document.createElement('div');
        articleCard.className = 'post-card';
        articleCard.innerHTML = `
            <div class="post-content">
                <h3><a href="${article.url}">${article.title}</a></h3>
                <time datetime="${article.date}">${formatDate(article.date)}</time>
                <div class="thumbnail-container" onclick="window.location.href='${article.url}'">
                    <img src="${article.image}" alt="${article.title}" class="post-thumbnail">
                </div>
                <p>${article.description}</p>
                <a href="${article.url}" class="read-more">阅读全文</a>
            </div>
        `;
        postList.appendChild(articleCard);
    });

    function formatDate(dateString) {
        const date = new Date(dateString);
        return `${date.getFullYear()}年${date.getMonth()+1}月${date.getDate()}日`;
    }
});
