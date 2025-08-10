// 联系表单处理
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
});