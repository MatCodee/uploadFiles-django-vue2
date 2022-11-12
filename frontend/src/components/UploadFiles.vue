<template>
    <div>
      <input v-model="form.title" type="text" class="form-control mb-3"  placeholder="title">
      <textarea v-model="form.description" class="form-control mb-3"  rows="3" placeholder="description"></textarea>
      <div v-if="progressInfos">
        <div class="mb-2"
          v-for="(progressInfo, index) in progressInfos"
          :key="index"
        >
          <span>{{progressInfo.fileName}}</span>
          <div class="progress">
            <div class="progress-bar progress-bar-info"
              role="progressbar"
              :aria-valuenow="progressInfo.percentage"
              aria-valuemin="0"
              aria-valuemax="100"
              :style="{ width: progressInfo.percentage + '%' }"
            >
              {{progressInfo.percentage}}%
            </div>
          </div>
        </div>
      </div>
  
      <label class="btn btn-default">
        <input type="file" multiple @change="selectFile" />
      </label>
  
      <button class="btn btn-success"
        :disabled="!selectedFiles"
        @click="saveBlog"
      >
        Upload
      </button>
  
      <div v-if="message" class="alert alert-light" role="alert">
        <ul>
          <li v-for="(ms, i) in message.split('\n')" :key="i">
            {{ ms }}
          </li>
        </ul>
      </div>
  
      <div class="card">
        <div class="card-header">List of Files</div>
        <ul class="list-group list-group-flush">
          <li class="list-group-item"
            v-for="(file, index) in fileInfos"
            :key="index"
          >
            <a :href="file.url">{{ file.name }}</a>
          </li>
        </ul>
      </div>
    </div>
  </template>

<script>
import UploadService from "../services/UploadFilesService";

export default {
  name: "upload-files",
  data() {
    return {
        form: {
          title: '',
          description: '',
        },
        selectedFiles: undefined,
        progressInfos: [],
        message: "",
        fileInfos: [],
    };
  },
  mounted() {
    //UploadService.getFiles().then((response) => { this.fileInfos = response.data;});
  },
  methods: {
    selectFile(event) {
      this.progressInfos = [];
      this.selectedFiles = event.target.files;
      console.log("entro aqui")
      console.log(event.target.files)
    },
    saveBlog() {
      if(this.form.title && this.form.description) {
        let form = {
          title: this.form.title,
          description: this.form.description,
        }
        UploadService.add_blog_to_database(form)
        .then((response) => {
          console.log(response.data)
          this.uploadFiles(response.data['id'])
        })
        .catch((e) =>{
          console.log(e)
        })
      }
    },  
    uploadFiles(id_blog) {
      this.message = "";
      console.log(this.selectedFiles.length)
      for (let i = 0; i < this.selectedFiles.length; i++) {
        this.upload(i, this.selectedFiles[i],id_blog);
      }
    },
    upload(idx, file,id_blog) {
      this.progressInfos[idx] = { percentage: 0, fileName: file.name };

      UploadService.upload(file,id_blog, (event) => {
        this.progressInfos[idx].percentage = Math.round(100 * event.loaded / event.total);
      })
        .then((response) => {
          let prevMessage = this.message ? this.message + "\n" : "";
          this.message = prevMessage + response.data.message;

          return UploadService.getFiles();
        })
        .then((files) => {
          this.fileInfos = files.data;
        })
        .catch(() => {
          this.progressInfos[idx].percentage = 0;
          this.message = "Could not upload the file:" + file.name;
        });
    }
  },
};
</script>

