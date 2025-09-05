---
layout: default
title: Welcome
---

<style>
  body {
    background-color: #f4f6f8; /* soft light gray */
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #34495e;
  }
  .header {
    text-align: center;
    margin-top: 50px;
    background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80'); /* gentle tech/abstract image */
    background-size: cover;
    background-position: center;
    padding: 80px 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
  .header h1 {
    font-size: 3em;
    margin: 0;
  }
  .header p {
    font-size: 1.3em;
    margin-top: 10px;
  }
  .content {
    max-width: 700px;
    margin: 50px auto;
    line-height: 1.8;
  }
  .content a {
    color: #2980b9;
    text-decoration: none;
  }
  .content a:hover {
    text-decoration: underline;
  }
</style>

<div class="header">
  <h1>Hi, I'm Siri!</h1>
  <p>Exploring tech, AI, and data science</p>
</div>

<div class="content">
---
layout: default
title: Welcome
---

<style>
  body {
    background-color: #f4f6f8; /* soft light gray */
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #34495e;
  }
  .header {
    text-align: center;
    margin-top: 50px;
    background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80'); /* gentle tech/abstract image */
    background-size: cover;
    background-position: center;
    padding: 80px 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
  .header h1 {
    font-size: 3em;
    margin: 0;
  }
  .header p {
    font-size: 1.3em;
    margin-top: 10px;
  }
  .content {
    max-width: 700px;
    margin: 50px auto;
    line-height: 1.8;
  }
  .content a {
    color: #2980b9;
    text-decoration: none;
  }
  .content a:hover {
    text-decoration: underline;
  }
</style>

<div class="header">
  <h1>Hi, I'm Siri!</h1>
  <p>Exploring tech, AI, and data science</p>
</div>

<div class="content">
  <h2>About Me</h2>
  <p>I'm passionate about technology, AI, and data science. I love learning new things and sharing insights through this blog. Here, you'll find my thoughts on tech, tutorials, and explorations in AI.</p>

  <h2>Latest Blog Posts</h2>
  <ul>
    {% for post in site.posts limit:5 %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%b %-d, %Y" }}
      </li>
    {% endfor %}
---
layout: default
title: Welcome
---

<style>
  body {
    background-color: #f4f6f8; /* soft light gray */
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #34495e;
  }

.header {
    text-align: center;
    margin-top: 50px;
    background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80'); /* gentle tech/abstract image */
    background-size: cover;
    background-position: center;
    padding: 80px 20px;
    border-radius: 15px;
    color: white;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
  }
 .header h1 {
    font-size: 3em;
    margin: 0;
  }
  .header p {
    font-size: 1.3em;
    margin-top: 10px;
  }
  .content {
    max-width: 700px;
    margin: 50px auto;
    line-height: 1.8;
  }
  .content a {
    color: #2980b9;
    text-decoration: none;
  }
  .content a:hover {
    text-decoration: underline;
  }

</style>

<div class="header">
  <h1>Hi, I'm Siri!</h1>
  <p>Exploring tech, AI, and data science</p>
</div>

<div class="content">
  <h2>About Me</h2>
  <p>I'm passionate about technology, AI, and data science. I love learning new things and sharing insights through this blog. Here, you'll find my thoughts on tech, tutorials, and explorations in AI.</p>

  <h2>Latest Blog Posts</h2>
  <ul>
    {% for post in site.posts limit:5 %}
      <li>
        <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%b %-d, %Y" }}
      </li>
    {% endfor %}
  </ul>
</div>

