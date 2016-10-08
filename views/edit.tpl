% rebase('base.tpl')

<div class="col-sm-9 col-sm-offset-3 col-md-10 col-offset-2 main">

  <!-- 登録 / 編集で見出しを切り替え -->
  % if request.path == "/books/add":
    <h1 class="page-header">登録</h1>
  % else:
    <h1 class="page-header">編集</h1>
  % end

  <!-- 登録 / 編集でformの中身を切り替え -->
  % if request.path == "/books/add":
    <form action="/books/add" method="post">
  % else:
    <form action="/books/{{ book.id }}/edit" method="post">
  % end

    <!-- タイトルのフォーム -->
    <div class="form-group">

      {{ !form.title.label }}
      {{ !form.title(class_="form-control", placeholder = u'タイトル', maxlength = "100") }}

      <!-- エラー時の内容表示 -->
      % if form.title.errors:
        <div class="errors">
          % for error in form.title.errors:
            <p class="text-danger">{{ error }}</p>
          % end
        </div>
      % end

    </div>

    <!-- 価格のフォーム -->
    <div class="form-group">

      {{ !form.price.label }}
      {{ !form.price(class_="form-control", placeholder = u'価格', maxlength = "100") }}

      <!-- エラー時の内容表示 -->
      % if form.price.errors:
        <div class="errors">
          % for error in form.price.errors:
            <p class="text-danger">{{ error }}</p>
          % end
        </div>
      % end

    </div>

    <!-- メモのフォーム -->
    <div class="form-group">

      {{ !form.memo.label }}
      {{ !form.memo(class_="form-control", placeholder = u'メモ', maxlength = "100") }}

      <!-- エラー時の内容表示 -->
      % if form.memo.errors:
        <div class="errors">
          % for error in form.memo.errors:
            <p class="text-danger">{{ error }}</p>
          % end
        </div>
      % end

    </div>

    <!-- 登録 / 編集でSubmitボタンを切り替え -->
    % if request.path == "/books/add":
      <input type="submit" class="btn btn-default" value="作成">
    % else:
      <input type="submit" class="btn btn-default" value="更新">
    % end

  </form>
</div>
