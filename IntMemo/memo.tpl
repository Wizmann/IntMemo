[Metadata]
{% for (key, value) in article.Metadata.items() %}
{{ key }}: {{ value }}
{% endfor %}

[Tags]
{% for (key, value) in article.Tags.items() %}
{{ key }}: {{ value }}
{% endfor %}

[Description]
{{ article.Description }}

[Process]
{{ article.Process | to_json }}

