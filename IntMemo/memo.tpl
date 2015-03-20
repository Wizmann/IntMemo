{%- for section in article -%}
{{ section.section }}
{{ section.content|strjoin }}
{%- endfor -%}
