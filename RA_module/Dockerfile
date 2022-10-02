
FROM pnp_1604_kinetic

### PNP packages ###

USER root

RUN apt-get update && \
    apt-get install -y ros-kinetic-rviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER robot

# Trick to disable cache from here
ADD http://worldtimeapi.org/api/ip /tmp/time.tmp 

COPY --chown=robot:robot ra_action /home/robot/src/ra_action
COPY --chown=robot:robot ra_action_msgs /home/robot/src/ra_action_msgs
COPY --chown=robot:robot ra_pnp /home/robot/src/ra_pnp

RUN cd $HOME/ros/catkin_ws/src && \
    ln -s $HOME/src/ra_action . && \
    ln -s $HOME/src/ra_action_msgs . && \
    ln -s $HOME/src/ra_pnp .

# Compile ROS packages

RUN /bin/bash -ci "cd $HOME/ros/catkin_ws; catkin_make -j1"


# Set working dir and container command

WORKDIR /home/robot

CMD /usr/bin/tmux


