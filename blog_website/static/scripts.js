// Flash message handling
document.querySelectorAll('.flash-message').forEach(function(message) {
    setTimeout(function() {
        message.classList.add('hidden');
        setTimeout(() => message.style.display = 'none', 300);
    }, 3000);
    const closeBtn = message.querySelector('.close-btn');
    if (closeBtn) {
        closeBtn.addEventListener('click', function() {
            message.classList.add('hidden');
            setTimeout(() => message.style.display = 'none', 300);
        });
    }
});

// Comment area toggle
document.querySelectorAll('.comment-span').forEach(span => {
    span.addEventListener('click', () => {
        const commentArea = span.closest('.post-preview').querySelector('.comment-area');
        if (commentArea.style.display === 'none' || commentArea.style.display === '') {
            commentArea.style.display = 'block';
        } else {
            commentArea.style.display = 'none';
        }
    });
});

// Like toggle
document.querySelectorAll('.like-span').forEach(span => {
    span.addEventListener('click', () => {
        span.classList.toggle('clicked');
        let likes = parseInt(span.getAttribute('data-likes'));
        if (span.classList.contains('clicked')) {
            likes += 1;
        } else {
            likes -= 1;
        }
        span.setAttribute('data-likes', likes);
        span.firstChild.textContent = likes;
    });
});
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.cancel-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const checkbox = this.closest('.comment-content').querySelector('.edit-toggle');
            if (checkbox) {
                checkbox.checked = false; // Unchecks the checkbox, hiding the form
            }
        });
    });
});