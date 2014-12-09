<html>

<head>
  <title>{% block title_content %}{% endblock %}</title>
  <link rel="stylesheet" href="/style.css" />
  <style>
  html, body {
    height: 100%;
    min-height: 100%;
  }

  .right {
    float: right;
  }

  .left {
    float: left;
  }

  .mainContainer {
    width: 80%;
    margin-left: 10%;
  }

  .messageCont {
    display: inline-block;
    width: 100%;
    border: 4px solid blue;
    height: 80%;
    border-radius: 4px;
  }

  .timerBox {
    width: auto;
    display: inline-block;
    text-align: center;
  }

  .messageBox {
    height: auto;
  }

  .message {
    border-bottom: 1px solid black;
    border-width: 80%;
  }

  .sendButton {
    width: 10%;
    display: inline-block;
    float: right;
  }

  </style>
</head>

<body>
  <span style="width: 100%; text-align: center;"><h1>Project Hermes </h1></span>
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
    <input type="text" name="message_content" style="width: 90%; display: inline-block;" />
    <button class="sendButton">This is button!</button>
  </div>
  </form>
</body>

</html>
