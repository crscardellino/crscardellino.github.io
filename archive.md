---
layout: page
title: Blog Archive
permalink: /archive/
image: "/assets/images/storm.jpg"
---

<section class="archive-post-list">
	{% for post in site.posts %}
       {% assign currentDate = post.date | date: "%Y" %}
       {% if currentDate != myDate %}
           {% unless forloop.first %}</ul>{% endunless %}
           <h3>{{ currentDate }}</h3>
           <ul>
           {% assign myDate = currentDate %}
       {% endif %}
       <li><span>{{ post.date | date: "%B %-d, %Y" }}</span> - <a href="{{ post.url }}">{{ post.title }}</a></li>
       {% if forloop.last %}</ul>{% endif %}
   {% endfor %}
</section>
