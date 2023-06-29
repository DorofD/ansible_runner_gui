import { io } from "socket.io-client";


var socket = io.connect('http://192.168.13.82:5000');


socket.on("connect", () => {
  socket.emit("connect_message", { data: "Client connected!" });
});


socket.on("message", (data) => {
  // alert(data.data)
  let new_li = document.createElement('li');
  new_li.innerHTML = data.data
  ul.append(new_li)
});


window.init_message = () => {
    socket.emit("init_message", { data: "init message" });
}


window.create_text = () => {
    let text_node = document.createTextNode('Новый текст');
    document.body.append(text_node);
}


window.add_li = () => {
    let new_li = document.createElement('li');
    new_li.innerHTML = 'element'
    ul.append(new_li)
  }
