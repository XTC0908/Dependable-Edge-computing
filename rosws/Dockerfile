FROM ros:kinetic
MAINTAINER Rui Chen <ruich@kth.se>

# install rosbridge server and supervisord
RUN apt-get update && apt-get install -y ros-kinetic-rosbridge-suite
RUN git clone https://github.com/XTC0908/Dependable-Edge-computing.git
RUN export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:./Dependable-Edge-computing/rosws
# serup supervisord.conf
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
# setup entrypoint
#COPY ./rosbridge_entrypoint.sh /

EXPOSE 9090

#ENTRYPOINT ["/rosbridge_entrypoint.sh"]

#ENTRYPOINT ["source ./Dependable-Edge-computing/rosws/start.sh"]
CMD ["/bin/bash"]