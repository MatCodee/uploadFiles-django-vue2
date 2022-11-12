<template>
  <div class="home">
     <div class="container">

          <div class="webflow-style-input">
            <input class="" type="email" placeholder="What's your email?" />
          </div>
          <div class="webflow-style-input">
            <textarea class="" type="email" placeholder="What's your email?" />
          </div>
          <div class="webflow-style-input-file">
            <input class="file-field-upload" type="file" @change="files_upload">
            <p>upload file here</p>
          </div>
          <button @click="upload">Upload</button>

     </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      title: '',
      description: '',
      files: []
    }
  },
  methods: {
    files_upload(event) {
      this.files = event.target.files;
    },
    async getUsers() {
        try{
          const response = await axios.get('users');
          console.log(response);
          this.users = response.data;
        } catch(error){
          console.log(error);
        }
    },
    async upload() {
      const url = "http://127.0.0.1:8000/blog/";
      
      let form = new FormData();
        form.append('title', this.title);
        form.append('description',this.description);
        form.append('files',this.files);
        await axios({
        method: 'post',
        headers: {"Content-type": "application/json"},
        url: url,
        data: form,
      })
      .then(function (response) {
        console.log(response.data)
      });
    }
  }
}
</script>
<style lang="scss">
/*
.container {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}



// reset
html { box-sizing: border-box; font-size: 10px; }
*, *:before, *:after { box-sizing: inherit; }
body, ul, li  { margin: 0; padding: 0; }
li { list-style: none; }
p, h1, h2, h3, h4, h5, h6 { margin-top: 0; }
a { text-decoration: none; }
input { border-style: none; background: transparent; outline: none; }
textarea { border-style: none; background: transparent; outline: none; overflow-y: hidden; }

button { padding: 0; background: none; border: none; outline: none; }

// some basic page styles
body {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: "Helvetica Neue",Helvetica,Arial,sans-serif;
  background-image: radial-gradient(circle at 0% 0%, #373b52, #252736 51%, #1d1e26);
}

// for demo
h1.demo {
  text-align: center;
  font-size: 2.4rem;
  font-weight: normal;
  margin-bottom: 1rem;
  color: #f5f6ff;
}
a.demo {
  text-align: center;
  font-size: 1.6rem;
  font-weight: normal;
  color: rgba(202, 205, 239, 0.8);
  margin-bottom: 3rem;
}
.demo-flex-spacer {
  flex-grow: 1;
}
.container {
  display: flex;
  flex-direction: column;
  //justify-content: center;
  height: 100vh;
  max-width: 1600px;
  padding: 0 15px;
  margin: 0 auto;
}

// colors
$input-background: rgba(57, 63, 84, 0.8);
$input-text-inactive: #7881A1;
$input-text-active: #BFD2FF;

// gradient animation
@keyframes gradient { 
  0%{background-position:0 0}
  100%{background-position:100% 0}
}

.webflow-style-input {
  position: relative;
  display: flex;
  flex-direction: row;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  border-radius: 2px;
  padding: 1.4rem 2rem 1.6rem;
  background: $input-background;
  margin-bottom: 20px;
  &:after {
    content: "";
    position: absolute;
    left: 0px;
    right: 0px;
    bottom: 0px;
    z-index: 999;
    height: 2px;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    background-position: 0% 0%;
    background: linear-gradient(to right, #B294FF, #57E6E6, #FEFFB8, #57E6E6, #B294FF, #57E6E6);
    background-size: 500% auto;
    animation: gradient 3s linear infinite;
  }
}

.webflow-style-input input {
  flex-grow: 1;
  color: $input-text-active;
  font-size: 1.8rem;
  line-height: 2.4rem;
  vertical-align: middle;
  &::-webkit-input-placeholder {
    color: $input-text-inactive;
  }
}

.webflow-style-input textarea {
  flex-grow: 1;
  color: $input-text-active;
  font-size: 1.8rem;
  line-height: 2.4rem;
  height: 100px;
  vertical-align: middle;
  &::-webkit-input-placeholder {
    color: $input-text-inactive;
  }
}


.webflow-style-input-file {
  position: relative;
  display: flex;
  flex-direction: row;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  border-radius: 2px;
  padding: 1.4rem 2rem 1.6rem;
  background: $input-background;
  margin-bottom: 20px;

  p {
    font-size: 2.2rem;
    color: $input-text-active;
  }
}

.file-field-upload {
  overflow: hidden;
  left: 0;
  top: 0;
  opacity: 0;
  position: absolute;
  font-size: 90px;
}


.webflow-style-input button {
  color:  $input-text-inactive;
  font-size: 2.4rem;
  line-height: 2.4rem;
  vertical-align: middle;
  transition: color .25s;
  &:hover {
    color: $input-text-active;
  }
}

button {
  width: 100%;
  max-width: 600px;
  color: $input-text-active;
  background-color: $input-background;
  padding: 20px 60px;
  font-size: 2.2rem;
  border-radius: 20px;
  cursor: pointer;
}
*/

</style>