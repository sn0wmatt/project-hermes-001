<html>

<head>
  <title>{% block title_content %}{% endblock %}</title>
  <link rel="stylesheet" href="/html/style.css" />
  
  <script type="text/javascript" src="/_ah/channel/jsapi"></script>
  <script src="/scripts/jquery.min.js" type="text/javascript"></script>
</head>

<body>
<script>
$(document).ready() {
  onOpened = function() {
    connected = true;
    // sendMessage('opened');
  };
  onMessage = function(msg) {
    alert(msg.data);
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

  $("#sendButton").submit(function(event) {

    event.preventDefault();

    var $form = $( this ),
    url = $form.attr( 'action' );

    var posting = $.post( url, { message_content: $('#message_content').val(), talk_key: {{ id }} } );

    posting.done(function( data ) {
      alert('success');
    });
  });
});
</script>





  <span style="width: 100%; text-align: center;"><h1>Project Hermes </h1></span>
  {% if talk.name == None %}
    {% if talk.host == user %}
      This chat has no name. Click <a href="/chatroomRename?talk_key={{ id }}">here</a> to name this chat!
    {% else %}
      This chat has no name.
    {% endif %}
  {% else %}
    {{ talk.name }}
  {% endif %}
  <form method="POST" action="/message?talk_key={{ id }}">
  <input type="hidden" name="talk_key" value="{{ id }}" />
  <div class="mainContainer">
    <div class="messageCont">
      <div class="messageBox" id="MessageBox">
      </div>
    </div>
    <input type="text" name="message_content" id="message_content" style="width: 90%; display: inline-block;" />
    <button id="sendButton" class="sendButton" onClick="sendMessage()">This is button!</button>
  </div>
  </form>
</body>

</html>
