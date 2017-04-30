$(document).ready(function() {

    $('.ui.dropdown').dropdown();
    $(".markas").click(function(){
        id=this.id
        val=$(this.closest('.dropdown')).dropdown('get value')
        console.log("/bookapi/")
        $.ajax({
            method:'post',
            url: "/bookapi/",
            success: function(result){
                console.log(result)},
            data:{book_id:id,mark_as:val}
        });
    });
  $('.ui.rating').rating('setting', 'onRate', function(value) {
      console.log('rating',value)
      id=$(this).attr('book')
      $.ajax({
            method:'post',
            url: "/bookapi/",
            success: function(result){
                console.log(result)},
            data:{book_id:id,rating:value}
        });
  });
  $('.follow').click(function () {
      id=this.id
      console.log(id)
      b=$(this)
       type=b.closest('div').attr('class')
      if(type.includes('cat')) {
          if (b.attr('class').includes('un')) {
              $.ajax({
                  method: 'post',
                  url: "/categorys/",
                  success: function (result) {
                      console.log(result)
                  },
                  data: {cat_id: id, follow: 0}
              });
              console.log('unfollow')
              b.text('follow')
          }

          else {
              $.ajax({
                  method: 'post',
                  url: "/categorys/",
                  success: function (result) {
                      console.log(result)
                  },
                  data: {cat_id: id, follow: 1}
              });
              console.log('follow')
              b.text('unfollow')
          }
      }
      else if(type.includes('auth')){
          if (b.attr('class').includes('un')) {
              $.ajax({
                  method: 'post',
                  url: "/authors/",
                  success: function (result) {
                      console.log(result)
                  },
                  data: {auth_id: id, follow: 0}
              });
              console.log('unfollow')
              b.text('follow')
          }

          else {
              $.ajax({
                  method: 'post',
                  url: "/authors/",
                  success: function (result) {
                      console.log(result)
                  },
                  data: {auth_id: id, follow: 1}
              });
              console.log('follow')
              b.text('unfollow')
          }
      }
      b.toggleClass('greay  un orange')
  })
  $('input.search').keyup(function () {
      key=$(this).val()
      console.log(key)
      if(/\S/.test(key)) {
          $.ajax({
              method: 'get',
              url: "/search/" + key,
              success: function (result) {
                  console.log(result, result.length)
                  items = ''
                  for (var b in result) {
                      items += "<a class='item' href='/book/" + result[b].id + "'>" + result[b].title + "</a>"
                  }
                  console.log(items)
                  $('.menu.search').html(items)

              },

          });
      }
      else{
          $('.menu.search').html('')
      }
  })
  $('#live_notify_list').click(function () {
      
  })
})
