<html>

<head>
  <title>{% block title_content %}{% endblock %}</title>
  <link rel="stylesheet" href="/style.css" />
</head>

<body>
  <form method="POST" action="/?talk_key={{ id }}">
  <div class="mainContainer">
    <div class="messageCont">
      <div class="messageBox" id="MessageBox">
        {% for message in talk.messages %}
          {% if message.author %}
            {{ message.author }}: {{ message.message }} <br/>
          {% else %}
            Anonymous: {{ message.message }}
          {% endif %}
        {% endfor %}
      </div>
    </div>
    <textarea name="message_content" style="width: 90%; display: inline-block;"></textarea>
    <button class="sendButton">This is button!</button>
  </div>
  </form>
</body>

</html>
