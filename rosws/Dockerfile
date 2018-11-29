FROM ros:kinetic
MAINTAINER Rui Chen <ruich@kth.se>

# install rosbridge server and supervisord
RUN apt-get update && apt-get install -y ros-kinetic-rosbridge-suite nano ros-kinetic-geographic-msgs
RUN git clone https://github.com/XTC0908/Dependable-Edge-computing.git
RUN export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/Dependable-Edge-computing/rosws
ENV ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/Dependable-Edge-computing/rosws
ENV PATH=$PATH:/opt/ros/kinetic/bin/
RUN rm -rf /Dependable-Edge-computing/rosws/devel
RUN rm -rf /Dependable-Edge-computing/rosws/build
RUN cp /Dependable-Edge-computing/rosws/start.bash /
RUN chmod +x /start.bash
#WORKDIR /Dependable-Edge-computing/rosws/
RUN ["/bin/bash", "-c", " source /opt/ros/kinetic/setup.sh && cd /Dependable-Edge-computing/rosws/ && catkin_make"]

# serup supervisord.conf
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# setup entrypoint
#COPY ./rosbridge_entrypoint.sh /

EXPOSE 9090

#ENTRYPOINT ["/rosbridge_entrypoint.sh"]

CMD ["/bin/bash"]
#, "-c", "/start.bash && tail -f /tmp/err_log.txt"]

#ENTRYPOINT ["/start.bash"]