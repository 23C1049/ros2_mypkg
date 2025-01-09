# SPDX-FileCopyrightText: 2024 Shizen Kotake
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    cigarettes_pub = launch_ros.actions.Node(
        package='mypkg',
        executable='cigarettes_pub',
        )
    cigarettes_sub = launch_ros.actions.Node(
        package='mypkg',
        executable='cigarettes_sub',
        output='screen'
        )

    return launch.LaunchDescription([cigarettes_pub,cigarettes_sub ])
