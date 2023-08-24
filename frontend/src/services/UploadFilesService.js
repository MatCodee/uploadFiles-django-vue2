import http from "../http-common";


class UploadFilesService {
  // Esta es la funcion que se va a agregar al backend directamente
  add_blog_to_database(form) {
    return http.post("blog/",form)
  }

  upload(file,id_blog, onUploadProgress) {
    let formData = new FormData();

    formData.append("file", file);
    formData.append("blog", id_blog);

    return http.post(`/upload/`, formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress
    });
  }

  getFiles() {
    return http.get("/files");
  }
}

export default new UploadFilesService();