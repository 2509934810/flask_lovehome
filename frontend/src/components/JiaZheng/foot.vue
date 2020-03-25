<template>
  <div class="foot container-fluid clear">
    <div class="container">
      <p>Copyright by Lovehome 2020</p>
      <a href="#">合作</a>
      <a href="#">招聘|</a>
      <a href="#">投资|</a>
      <a href="#">技术支持|</a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'foot',
  data () {
    return {
      msg: ''
    }
  }
}
</script>

<style lang="">
  .clear:before{content: ''; display: block;}
  .container-fluid{width: 100%; position: relactive}
  .container{width: 80%; margin: 0 auto}
  .foot{margin-top: 80px; height: 50px; line-height: 50px; background-color:lightseagreen; position: relative;}
  .foot p{float: left;}
  .foot a{float: right; margin-right: 20px;}
</style>
