import warnings
warnings.filterwarnings("ignore")

import genesis as gs

########################## init ##########################
gs.init(backend=gs.cpu)

########################## create a scene and entities ##########################
scene = gs.Scene(show_viewer=False)
# plane = scene.add_entity(gs.morphs.Plane())
robot = scene.add_entity(
    gs.morphs.MJCF(file='../../genesis/assets/xml/x1/mjcf/xyber_x1_flat.xml'),
)

########################## build ##########################
scene.build()
state = scene.get_state()

########################## joint names ##########################
leg_joint_names = ['left_hip_pitch', 'left_hip_roll', 'left_hip_yaw', 'left_knee_pitch',
             'left_ankle_pitch', 'left_ankle_roll', 'right_hip_pitch', 'right_hip_roll',
             'right_hip_yaw', 'right_knee_pitch', 'right_ankle_pitch', 'right_ankle_roll']
arm_joint_names = ['left_shoulder_pitch', 'left_shoulder_roll', 'left_shoulder_yaw', 'left_elbow_pitch',
                   'left_elbow_yaw', 'left_wrist_pitch', 'left_wrist_roll',
                   'right_shoulder_pitch', 'right_shoulder_roll', 'right_shoulder_yaw', 'right_elbow_pitch',
                   'right_elbow_yaw', 'right_wrist_pitch', 'right_wrist_roll']

dofs_idx = [robot.get_joint(name).dof_idx_local for name in arm_joint_names]
print(f'dofs idx: {dofs_idx}')

########################## dof positions ##########################
dof_positions = robot.get_dofs_position(dofs_idx)
print(f'dof positions: {dof_positions}')

########################## end effectors ##########################
end_effector_names = ['left_wrist_roll_link', 'right_wrist_roll_link']
effector_pos = robot.get_links_pos()
end_effector = [robot.get_link(name) for name in end_effector_names]
