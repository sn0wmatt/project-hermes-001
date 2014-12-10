<html>

<head>
  <title>{% block title_content %}{% endblock %}</title>
  <link rel="stylesheet" href="/html/style.css" />
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
  <script type="text/javascript" src="/_ah/channel/jsapi"></script>
  <script src="/scripts/jquery.min.js" type="text/javascript"></script>
</head>

<body>
<script>
$(document).ready(function() {

  onOpened = function() {
    connected = true;
    // sendMessage('opened');
  };
  onMessage = function(msg) {
    $('#MessageBox').append(msg.data + '<hr />')
  };
  onError = function(err) {
    //    alert(err);
  };
  onClose = function() {
    // alert("close");
    //   connected = false;
  };
  // open new session
  channel = new goog.appengine.Channel('{{ token }}');
  socket = channel.open();
  socket.onopen = onOpened;
  socket.onmessage = onMessage;
  socket.onerror = onError;
  socket.onclose = onClose;

  $("#formID").submit(function(event) {

    event.preventDefault();

    var $form = $( this ),
    url = $form.attr( 'action' );

    var posting = $.post( url, { message_content: $('#message_content').val(), talk_key: {{ id }} } );
  });
});
</script>





  <span style="width: 100%; text-align: center;"><h1>Project Hermes </h1></span>

  <div style="width: 100%; text-align: center;">
    {% if talk.name == None %}
      {% if talk.host == user %}
        This chat has no name. Click <a href="/chatroomRename?talk_key={{ id }}">here</a> to name this chat!
      {% else %}
        This chat has no name.
      {% endif %}
    {% else %}
      {{ talk.name }}
    {% endif %}
  </div>
  <form id="formID" method="POST" action="/message?talk_key={{ id }}">
  <input type="hidden" name="talk_key" value="{{ id }}" />
  <div class="mainContainer">
    <div class="messageCont">
      <div class="messageBox" id="MessageBox">
      </div>
    </div>
    <input type="text" name="message_content" id="message_content" style="width: 90%; display: inline-block;" />
    <button type="submit" id="sendButton" class="sendButton">Go</button>
  </div>
  </form>
</body>

</html>
