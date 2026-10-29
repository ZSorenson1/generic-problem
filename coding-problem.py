class Camera:
    def __init__(self, light_range, dist_range):
        self.light_range = light_range
        self.dist_range = dist_range


def cameras_in_range(sw_dist, sw_light, hw_cameras):

    c_dist =  sw_dist[0]
    #set current distance and then make sure all light values are covered at that distance
    while c_dist <= sw_dist[1]:
        c_light = sw_light[0]
        while c_light <= sw_light[1]:

            covered = False

            for cam in hw_cameras:
                if(cam.dist_range[0] <= c_light <= cam.dist_range[1] and
                   cam.light_range[0] <= c_light <= cam.light_range[1]):
                    covered = True 
                    break #no need to keep checking if this spot is covered
            
            #if any intersection of distance and light is not found our set of hardware cameras is invalid
            if not covered:
                return False 

            #assuming these are all integers for simplicity
            c_light += 1
        c_dist += 1 

    return True
