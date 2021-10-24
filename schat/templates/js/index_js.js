const socket = io({ path: "/sio/socket.io" });

socket.on("connect", () =>{
    console.log("Connected!");
    socket.emit("who_are_you", $('#user_name').val());
});

socket.on("disconnect", () =>{
    console.log("Lost connection to the server!");
});

$("#user_name").on("blur", (event) => {
    alert('Changed nick!');
    socket.emit("change_nickname", $('#user_name').val());
});


$("#form").submit( event => {
    event.preventDefault();
    socket.emit("message", $('#user_name').val() + ":   " + $("#message").val());
    $("#message").value = "";
    return false;
});

socket.on("response", message => {
    console.log("response:", message);
    var new_li = $(`<li style="display: none;" class="single-mess"></li>`).text(message);
    $("#messages").append(new_li);
    new_li.show("slow");
    console.log($(".single-mess").length);
    if ($(".single-mess").length >= 10){
        $(".single-mess:first-child").animate(
            { height: "-0px" },
            "slow",
            function(){ $(this).remove(); }
        );
    }
});
