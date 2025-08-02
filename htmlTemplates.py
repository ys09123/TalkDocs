css = '''
<style>
body {
    background-color: #e5ddd5;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.chat-message {
    display: flex;
    margin: 10px 0;
    align-items: flex-end;
}

.chat-message.user {
    justify-content: flex-end;
}

.chat-message.bot {
    justify-content: flex-start;
}

.chat-message .avatar {
    width: 40px;
    height: 40px;
    margin: 0 10px;
    flex-shrink: 0;
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    max-width: 70%;
    padding: 0.75rem 1rem;
    border-radius: 1rem;
    position: relative;
    font-size: 0.95rem;
    line-height: 1.4;
    word-wrap: break-word;
}

/* Bot (left-aligned) bubble */
.chat-message.bot .message {
    background-color: #ffffff;
    color: #000;
    border-top-left-radius: 0;
}

/* User (right-aligned) bubble */
.chat-message.user .message {
    background-color: #34eb8c;
    color: #000;
    border-top-right-radius: 0;
}
@keyframes blink {
    0% { opacity: 0.2; }
    20% { opacity: 1; }
    100% { opacity: 0.2; }
}
.dot {
    animation: blink 1.4s infinite;
    animation-delay: 0s;
}
.dot:nth-child(2) {
    animation-delay: 0.2s;
}
.dot:nth-child(3) {
    animation-delay: 0.4s;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1221348467/vector/chat-bot-ai-and-customer-service-support-concept-vector-flat-person-illustration-smiling.jpg?s=612x612&w=0&k=20&c=emMSOYb4jWIVQQBVpYvP9LzGwPXXhcmbpZHlE6wgR78=" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''


user_template = '''
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
    <div class="avatar">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_InUxO_6BhylxYbs67DY7-xF0TmEYPW4dQQ&s" alt="User Avatar">
    </div>
</div>
'''
