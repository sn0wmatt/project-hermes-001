<html>
<head>
{% block title%}{% endblock %}
</head>
<body>
{% for each in query_results %}
<a href="../chatroom?talk_key={{ each.talk_key }}">{{ each.name }}</a><br/>
{% endfor %}
</body>
</html>
