package test;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientBuilder;

public class test1 {
	
	public static void main(String[ ] args) {
		//Docker Client
		DockerClient  dockerClient = DockerClientBuilder.getInstance().build();
		

		//List Images
		for (com.github.dockerjava.api.model.Image images: dockerClient.listImagesCmd().withShowAll(true).exec()) {
	    	System.out.println(images);
		}
		
		//List Container
	    for (com.github.dockerjava.api.model.Container containers: dockerClient.listContainersCmd().withShowAll(true).exec()) {
	    	//dockerClient.startContainerCmd(containers.getId()).exec();
	    	System.out.println(containers);
	    	//dockerClient.stopContainerCmd(containers.getId()).exec();
	    	//dockerClient.killContainerCmd(containers.getId()).exec();
	    }
	    
	    //build an image from dockerfile
	    //String imageId = dockerClient.buildImageCmd().withDockerfile(new File("./dockerfile")).withPull(true).exec(new BuildImageResultCallback()).awaitImageId();
		
		
		
	}
}
