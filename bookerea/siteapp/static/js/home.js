$(document).ready(function() {
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
      b=$(this)
      if (b.attr('class').includes('un')){
          $.ajax({
            method:'post',
            url: "/categorys/",
            success: function(result){
                console.log(result)},
            data:{cat_id:id,follow:0}
        });
          console.log('unfollow')
          b.text('follow')
      }

      else
      {
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
      b.toggleClass('greay  un orange')
  })
})