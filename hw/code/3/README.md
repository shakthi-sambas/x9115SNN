DevOps-HomeWork3
================
The source code files for HW3 main.js, index.html and load balancer.js files are placed in src folder. 

Screen Shot Redis Server in Action
----------------------------------

![Alt text](./screen_shots/redis_cache_server.png/ "Redis Server")


---

Screen Shots for Express Server
---------------------------------

####Screen_Shot Express Server

![Alt text](./screen_shots/Node_3000.png/ "Express Server")

####Screen_Shot Express Server Command OutPut 1

![Alt text](./screen_shots/server_output1.png/ "Express Server Cmd 1")

####Screen_Shot Express Server Command OutPut 1

![Alt text](./screen_shots/server_output2.png/ "Express Server Cmd 2")

Screen Shots for Cache SET/GET
---------------------------------

####Screen_Shot Cache Set

![Alt text](./screen_shots/set.png/ "set")

####Screen_Shot Cache Get

![Alt text](./screen_shots/Node_get.png/ "get")

####Screen_Shot Cache Get Null

![Alt text](./screen_shots/Node_get_Null.png/ "get null")

---

Screen Shots for Recently Visted Sites
--------------------------------------

Here I used Redis lpush, ltrim and lrange to show the recently visited sites

```
  .....
  console.log(req.method, req.url);
	client.lpush(["sites", req.url], function(err, reply){
	})
	client.ltrim("sites", 0, 4)
	.....

```

____

```
  ...
  var temp = ""
		var w = client.lrange("sites", 0, 4, function(err, result){
			console.log("Recently visited sites are : " + result)
			.....
```

####Screen_Shot Recent 

![Alt text](./screen_shots/recent1.png/ "Recent")

####Screen_Shot Recent Command Output

![Alt text](./screen_shots/recent_cmd.png/ "Recent Cmd Output")

Screen Shots for Cat picture uploads: queue
-------------------------------------------

####Screen_Shot upload

![Alt text](./screen_shots/upload.png/ "upload")

####Screen_Shot meow

![Alt text](./screen_shots/meow.png/ "meow")

####Screen_Shot Empty Queue

![Alt text](./screen_shots/empty_queue.png/ "empty Queue")

---

Screen Shots for multiple Express Server Running
------------------------------------------------

####Screen_Shot Multiple Server 1

![Alt text](./screen_shots/multiple_server1.png/ "multiple_server1")

####Screen_Shot Multiple Server 2

![Alt text](./screen_shots/multilple_server2.png/ "multiple_server2")

####Screen_Shot Multiple Server 3

![Alt text](./screen_shots/multiple_server3.png/ "multiple_server3")

####Screen_Shot Multiple Server 4

![Alt text](./screen_shots/multiple_server4.png/ "multiple_server4")

---

Screen Shots for Proxy Load Balancer in Action
------------------------------------------------

####Screen_Shot Proxy Load Balancer Commnad Line

![Alt text](./screen_shots/node_balancer.png/ "Proxy Commnad Line output")

####Screen_Shot Load Balancer (Round Robin to Server1)

![Alt text](./screen_shots/lb1.png/ "Load Balancer Sceen1")

####Screen_Shot Load Balancer (Round Robin to Server2)

![Alt text](./screen_shots/lb2.png/ "Load Balancer Sceen2")

####Screen_ShotLoad Balancer (Round Robin to Server3)

![Alt text](./screen_shots/lb3.png/ "Load Balancer Sceen 3")

---


