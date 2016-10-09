<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>書籍管理</title>
    <link rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
          crossorigin="anonymous">
    <link rel="stylesheet" href="/css/style.css">
  </head>
  <body>

    <nav class="navbar navbar-inverse">
      <div class="navbar-header">
        <a href="#" class="navbar-brand">書籍管理アプリケーション</a>
      </div>
    </nav>

    <div class="container">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">

          <!-- request.pathの値でサイドメニューにハイライトをつける -->
          <ul class="nav nav-sidebar">
            % if request.path == "/books":
              <li class="active"><a href="/books">一覧</a></li>
              <li><a href="/books/add">登録</a></li>

            % elif request.path == "/books/add":
              <li><a href="/books">一覧</a></li>
              <li class="active"><a href="/books/add">登録</a></li>

            % else:
              <li class="active"><a href="/books">一覧</a></li>
              <li><a href="/books/add">登録</a></li>

            % end
          </ul>

        </div>

        {{!base}}

      </div>
    </div>

  </body>
</html>
