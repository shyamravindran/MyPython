package main

import ("fmt"
	"os/exec"
)

var VCenterHost= "shyam"
var VCenterUser= "shalu"
var VCenterPassword= "unni"
var Datacenter= "padma"
var Host= "ravi"
var Password= "janaki"
func main() {
 	
 	cmnd := exec.Command("./argsParse","-vh ",VCenterHost,
 		"-vu ",VCenterUser,
 		"-vp ",VCenterPassword,
 		"-dn ",Datacenter,
 		"-hh ",Host,
 		"-hp ",Password).Output()
 		
// 	if err != nil {		fmt.Println("error")
 //	}
 	fmt.Println(cmnd)
 
 }
