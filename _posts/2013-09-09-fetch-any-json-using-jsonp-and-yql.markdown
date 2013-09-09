---
layout: post
title: "Fetch any JSON using JSONP and YQL"
date: 2013-09-09
published: true
---

When building web applications, you sometimes want to retrieve JSON data from APIs and domains that are external to your service. Because of the [Same Origin policy](http://en.wikipedia.org/wiki/Same-origin_policy) in browsers, you cannot retrieve data from other domains via AJAX.

### JSON-P to the rescue

Usually to get around this, APIs will have endpoints that support [JSON-P](http://en.wikipedia.org/wiki/JSONP). JSON-P is a nifty technique that loads JSON data via `<script>` tags instead of loading the data via XMLHttpRequests (AJAX). To understand this, let's look at an example.

Let's say you have a service on `http://myservice.com/data.json` that returns the following JSON.

```js
{
  "from": "myservice",
  "status": 200,
  "data": ['foo', 'bar', 'baz'],
}
```

An application that lives on `http://anotherapplication.com` cannot access data.json in client-side JS via AJAX because `anotherapplication.com` and `myservice.com` are not the same domain. 

As the author of `myservice.com`, you can solve this problem by turning your JSON endpoint into a JSON-P endpoint. To do this you write `myservice.com` in such a way that hitting `http://myservice.com/data.json?callback=procedureName` returns the following:

```js
procedureName({
  "from": "myservice",
  "status": 200,
  "data": ['foo', 'bar', 'baz'],
})
```

Now, the author of `anotherapplication.com` can load data.json by adding the following script tag dynamically to the client side DOM.

```html
<script type="text/javascript" src="http://myservice.com/data.json?callback=procedureName">
```

Now, the function `procedureName` will get called with the data from data.json.

### Where YQL Comes in

Most web services will support JSON-P if they expect you to retrieve their data on the client side, but some do not.

For services that do not support JSON-P that live on the internet, you can use [YQL](http://developer.yahoo.com/yql/) to proxy the request through Yahoo's servers, and retrieve data in the same way.

Here is a snippet of jQuery code that would normally hit `http://myservice.com/data.json`

```js

$.ajax({
  'url': 'http://myservice.com/data.json',
  'dataType': 'json',
  'success': function(response) {
    console.log(response);
  },
});
```

Here is how you modify it to proxy via Yahoo's servers.

```js

var yql_url = 'https://query.yahooapis.com/v1/public/yql';

$.ajax({
  'url': yql_url,
  'data': {
    'q': 'SELECT * FROM json WHERE url="'+yql_url+'"',
    'format': 'json',
    'jsonCompat': 'new',
  },
  'dataType': 'jsonp',
  'success': function(response) {
    console.log(response);
  },
});
```

Using this trick, does mean that you have to trust `http://myservice.com`, because any content returned by it can get executed by your client side JS. It also means that `http://myservice.com` needs to live on the open web (not on an internal server), so that Yahoo servers can hit it.

jQuery will automatically add a `callback` parameter to the request, and give that name to the `success` function, so that it gets called appropriately.
