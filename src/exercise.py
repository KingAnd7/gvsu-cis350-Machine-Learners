class Exercise:
    """
    The exercise class handles the list of exercises the user can add to their workouts.
    """
    def __init__(self, name="None", sets=0, reps=0, muscle_group1="None", muscle_group2="None", summary='',
     equipment_required='None') -> None:
        """
        Initializer for the EXERCISE class.
        """
        self.name = name
        self.sets = sets
        self.reps = reps
        self.muscle_group1 = muscle_group1
        self.muscle_group2 = muscle_group2
        self.summary = summary
        self.equipment_required = equipment_required

    # Getters for each instance variable
    def get_name(self):
        return self.name

    def get_sets(self):
        return self.sets

    def get_reps(self):
        return self.reps

    def get_muscle_group1(self):
        return self.muscle_group1

    def get_muscle_group2(self):
        return self.muscle_group2

    def get_summary(self):
        return self.summary

    def get_equipment_required(self):
        return self.equipment_required

    # Setters for each instance variable
    def set_name(self, name):
        self.name = name

    def set_sets(self, sets):
        self.sets = sets

    def set_reps(self, reps):
        self.reps = reps

    def set_muscle_group1(self, muscle_group1):
        self.muscle_group1 = muscle_group1

    def set_muscle_group2(self, muscle_group2):
        self.muscle_group2 = muscle_group2

    def set_summary(self, summary):
        self.summary = summary

    def set_equipment_required(self, equipment_required):
        self.equipment_required = equipment_required

# Example of exercises, maybe we want to add a way to make your own..?
movements = []

bench_press = Exercise("Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on a flat bench, grip the barbell, and press it from your chest to arms fully extended.", "Barbell, Bench")
movements.append(bench_press)

inc_bench_press = Exercise("Incline Barbell Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on an incline bench, grip the barbell, and press it from your chest to arms fully extended.", "Barbell, Incline Bench")
movements.append(inc_bench_press)

chest_press = Exercise("Chest Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Sit on a chest press machine and press the handles forward until arms are fully extended.", "Chest Press Machine")
movements.append(chest_press)

dumbbell_fly = Exercise("Dumbbell Fly", 0, 0, "Chest", "Front Deltoids", "Lie on a flat bench with dumbbells in hand, lower arms out to sides, then bring them together above your chest.", "Dumbbells, Bench")
movements.append(dumbbell_fly)

cable_fly = Exercise("Cable Fly", 0, 0, "Chest", "Front Deltoids", "Stand between cable machines, grab the handles, and pull them together in front of you while maintaining slightly bent arms.", "Cable Machine")
movements.append(cable_fly)

dips = Exercise("Dips", 0, 0, "Chest", "Triceps, Deltoids", "Grip parallel bars and lower your body until your arms are at 90 degrees, then push back up.", "Parallel Bars")
movements.append(dips)

tricep_pushdown = Exercise("Tricep Pushdown", 0, 0, "Triceps", "", "Using a cable machine, grip the bar and push it down until your arms are fully extended.", "Cable Machine")
movements.append(tricep_pushdown)

skull_crusher = Exercise("Skull Crusher", 0, 0, "Triceps", "", "Lie on a bench with an EZ bar and lower it toward your forehead, then extend your arms to press the bar back up.", "EZ Bar, Bench")
movements.append(skull_crusher)

squat = Exercise("Barbell Squat", 0, 0, "Quads", "Glutes, Hamstrings", "Stand with feet shoulder-width apart, barbell on upper back, and lower yourself into a squat before standing back up.", "Barbell")
movements.append(squat)

deadlift = Exercise("Deadlift", 0, 0, "Back", "Hamstrings, Glutes", "Grip the barbell on the floor, hinge at the hips, and lift the bar while keeping your back straight.", "Barbell")
movements.append(deadlift)

romanian_deadlift = Exercise("Romanian Deadlift", 0, 0, "Hamstrings", "Glutes", "With a barbell, lower it by hinging at the hips while keeping your legs straight, then return to standing.", "Barbell")
movements.append(romanian_deadlift)

leg_press = Exercise("Leg Press", 0, 0, "Quads", "Glutes", "Sit on the leg press machine, place feet on the platform, and push it away by extending your legs.", "Leg Press Machine")
movements.append(leg_press)

lunges = Exercise("Lunges", 0, 0, "Quads", "Glutes, Hamstrings", "Step forward with one leg, lower your hips until both knees are at 90-degree angles, and push back up.", "Dumbbells (optional)")
movements.append(lunges)

calf_raise = Exercise("Calf Raise", 0, 0, "Calves", "", "Stand on a raised surface, lift your heels off the ground by contracting your calves, then lower them back down.", "Calf Raise Machine or Dumbbells")
movements.append(calf_raise)

lat_pull_down = Exercise("Lat Pull Down", 0, 0, "Back", "Biceps", "Sit at a lat pull-down machine, grip the bar, and pull it down to your chest while keeping your back straight.", "Lat Pull-Down Machine")
movements.append(lat_pull_down)

pull_up = Exercise("Pull Up", 0, 0, "Back", "Biceps", "Grip a pull-up bar with palms facing away and pull your body up until your chin is over the bar.", "Pull-Up Bar")
movements.append(pull_up)

barbell_row = Exercise("Barbell Row", 0, 0, "Back", "Biceps", "Bend over with a barbell and row it to your lower chest, keeping your back straight.", "Barbell")
movements.append(barbell_row)

dumbbell_row = Exercise("Dumbbell Row", 0, 0, "Back", "Biceps", "Place one knee on a bench, grip a dumbbell with the other hand, and row it to your side while keeping your back straight.", "Dumbbell, Bench")
movements.append(dumbbell_row)

shoulder_press = Exercise("Shoulder Press", 0, 0, "Shoulders", "Triceps", "Grip a barbell or dumbbells at shoulder height and press them overhead until your arms are fully extended.", "Barbell or Dumbbells")
movements.append(shoulder_press)

lateral_raise = Exercise("Lateral Raise", 0, 0, "Shoulders", "", "Stand with dumbbells at your sides and lift them out to the sides until your arms are parallel to the floor.", "Dumbbells")
movements.append(lateral_raise)

front_raise = Exercise("Front Raise", 0, 0, "Shoulders", "Front Deltoids", "Hold dumbbells in front of your thighs and raise them in front of you until your arms are parallel to the floor.", "Dumbbells")
movements.append(front_raise)

face_pull = Exercise("Face Pull", 0, 0, "Shoulders", "Rear Deltoids", "Using a cable machine with a rope attachment, pull the rope toward your face, keeping your elbows high.", "Cable Machine")
movements.append(face_pull)

bicep_curl = Exercise("Bicep Curl", 0, 0, "Biceps", "", "Stand with dumbbells or a barbell and curl the weights up to your shoulders while keeping your elbows stationary.", "Dumbbells or Barbell")
movements.append(bicep_curl)

hammer_curl = Exercise("Hammer Curl", 0, 0, "Biceps", "Forearms", "Hold dumbbells with palms facing each other and curl them toward your shoulders.", "Dumbbells")
movements.append(hammer_curl)

preacher_curl = Exercise("Preacher Curl", 0, 0, "Biceps", "", "Sit at a preacher bench with an EZ bar and curl the bar toward your shoulders while keeping your upper arms on the pad.", "EZ Bar, Preacher Curl Bench")
movements.append(preacher_curl)

plank = Exercise("Plank", 0, 0, "Core", "", "Hold a position with your forearms and toes on the ground, keeping your body straight and core engaged.", "None")
movements.append(plank)

sit_up = Exercise("Sit-Up", 0, 0, "Core", "", "Lie on your back with knees bent, then sit up toward your knees and lower back down.", "None")
movements.append(sit_up)

russian_twist = Exercise("Russian Twist", 0, 0, "Core", "Obliques", "Sit on the floor, lean back slightly, and twist your torso side to side while holding a weight or medicine ball.", "Medicine Ball or Dumbbell")
movements.append(russian_twist)
# Assuming `Exercise` is already defined, and `movements` list is initialized

push_up = Exercise("Push-Up", 0, 0, "Chest", "Triceps, Front Deltoids", "Start in a plank position and lower your chest to the ground, then push back up.", "None")
movements.append(push_up)

close_grip_bench_press = Exercise("Close-Grip Bench Press", 0, 0, "Triceps", "Chest, Front Deltoids", "Perform a bench press with a narrow grip to target the triceps.", "Barbell, Bench")
movements.append(close_grip_bench_press)

pec_dec_fly = Exercise("Pec Dec Fly", 0, 0, "Chest", "Front Deltoids", "Sit at a pec dec machine and bring your arms together in front of your chest.", "Pec Dec Machine")
movements.append(pec_dec_fly)

reverse_grip_pull_down = Exercise("Reverse Grip Pull Down", 0, 0, "Back", "Biceps", "Sit at a lat pull-down machine with an underhand grip and pull the bar to your chest.", "Lat Pull-Down Machine")
movements.append(reverse_grip_pull_down)

seated_row = Exercise("Seated Row", 0, 0, "Back", "Biceps, Rear Deltoids", "Sit at a cable row machine and pull the handles toward your torso while keeping your back straight.", "Cable Row Machine")
movements.append(seated_row)

t_bar_row = Exercise("T-Bar Row", 0, 0, "Back", "Biceps", "Stand with a T-bar handle and pull the weight toward your torso.", "T-Bar Row Machine or Landmine Attachment")
movements.append(t_bar_row)

shrug = Exercise("Barbell Shrug", 0, 0, "Traps", "", "Hold a barbell with arms at your sides and shrug your shoulders upward.", "Barbell")
movements.append(shrug)

rear_delt_fly = Exercise("Rear Delt Fly", 0, 0, "Shoulders", "Rear Deltoids", "Bend over with dumbbells and raise your arms to the sides to target the rear deltoids.", "Dumbbells")
movements.append(rear_delt_fly)

arnold_press = Exercise("Arnold Press", 0, 0, "Shoulders", "Triceps", "Begin with dumbbells at shoulder height and rotate your arms as you press them overhead.", "Dumbbells")
movements.append(arnold_press)

overhead_tricep_extension = Exercise("Overhead Tricep Extension", 0, 0, "Triceps", "", "Hold a dumbbell or bar overhead and lower it behind your head, then extend your arms to press back up.", "Dumbbell or Barbell")
movements.append(overhead_tricep_extension)

# Lower Body Exercises
goblet_squat = Exercise("Goblet Squat", 0, 0, "Quads", "Glutes", "Hold a dumbbell close to your chest and perform a squat.", "Dumbbell")
movements.append(goblet_squat)

bulgarian_split_squat = Exercise("Bulgarian Split Squat", 0, 0, "Quads", "Glutes, Hamstrings", "Place one foot on a bench behind you and lower into a squat on the standing leg.", "Bench, Dumbbell (optional)")
movements.append(bulgarian_split_squat)

glute_bridge = Exercise("Glute Bridge", 0, 0, "Glutes", "Hamstrings", "Lie on your back with knees bent and lift your hips by squeezing the glutes.", "None (optional: Barbell or Dumbbell for added resistance)")
movements.append(glute_bridge)

hip_thrust = Exercise("Hip Thrust", 0, 0, "Glutes", "Hamstrings, Quads", "Sit with your upper back on a bench, place a barbell on your hips, and thrust them upward.", "Barbell, Bench")
movements.append(hip_thrust)

leg_extension = Exercise("Leg Extension", 0, 0, "Quads", "", "Sit on a leg extension machine and extend your knees to lift the weight.", "Leg Extension Machine")
movements.append(leg_extension)

lying_leg_curl = Exercise("Lying Leg Curl", 0, 0, "Hamstrings", "", "Lie face down on a leg curl machine and curl your legs up toward your glutes.", "Lying Leg Curl Machine")
movements.append(lying_leg_curl)

standing_calf_raise = Exercise("Standing Calf Raise", 0, 0, "Calves", "", "Stand on a calf raise machine or platform and lift your heels off the ground.", "Standing Calf Raise Machine or Raised Platform")
movements.append(standing_calf_raise)

seated_calf_raise = Exercise("Seated Calf Raise", 0, 0, "Calves", "", "Sit at a calf raise machine and raise your heels by pressing through the balls of your feet.", "Seated Calf Raise Machine")
movements.append(seated_calf_raise)

# Core Exercises
leg_raise = Exercise("Leg Raise", 0, 0, "Core", "Hip Flexors", "Lie on your back and lift your legs to 90 degrees, then lower them without touching the floor.", "None (optional: Ankle Weights for added resistance)")
movements.append(leg_raise)

mountain_climbers = Exercise("Mountain Climbers", 0, 0, "Core", "Shoulders, Hip Flexors", "Start in a plank position and alternate driving your knees toward your chest.", "None")
movements.append(mountain_climbers)

hanging_leg_raise = Exercise("Hanging Leg Raise", 0, 0, "Core", "Hip Flexors", "Hang from a bar and lift your legs until they are parallel to the ground, then lower.", "Pull-up Bar or Hanging Leg Raise Station")
movements.append(hanging_leg_raise)

bicycle_crunch = Exercise("Bicycle Crunch", 0, 0, "Core", "Obliques", "Lie on your back, bring one knee toward the opposite elbow, and alternate sides in a pedaling motion.", "None")
movements.append(bicycle_crunch)

# Additional Movements
kettlebell_swing = Exercise("Kettlebell Swing", 0, 0, "Glutes", "Hamstrings, Core", "Hold a kettlebell with both hands and swing it forward using a hip hinge motion.", "Kettlebell")
movements.append(kettlebell_swing)

farmer_walk = Exercise("Farmer's Walk", 0, 0, "Core", "Forearms, Shoulders", "Hold a weight in each hand and walk a specified distance while keeping your core tight.", "Dumbbells, Kettlebells, or Farmer's Walk Handles")
movements.append(farmer_walk)

sled_push = Exercise("Sled Push", 0, 0, "Legs", "Glutes, Core", "Push a weighted sled forward over a specified distance.", "Sled (Weighted Sled)")
movements.append(sled_push)

landmine_press = Exercise("Landmine Press", 0, 0, "Shoulders", "Chest, Triceps", "Hold a barbell anchored on the floor and press it forward in a standing or kneeling position.", "Landmine Attachment, Barbell")
movements.append(landmine_press)

# Olympic Lifts
power_clean = Exercise("Power Clean", 0, 0, "Full Body", "Quads, Glutes, Back", "Lift a barbell from the ground to shoulder height in one explosive movement.", "Barbell, Weight Plates")
movements.append(power_clean)

clean_and_jerk = Exercise("Clean and Jerk", 0, 0, "Full Body", "Quads, Glutes, Shoulders", "Lift a barbell from the ground to overhead in two movements: clean and jerk.", "Barbell, Weight Plates")
movements.append(clean_and_jerk)

snatch = Exercise("Snatch", 0, 0, "Full Body", "Quads, Glutes, Shoulders", "Lift a barbell from the ground to overhead in one continuous motion.", "Barbell, Weight Plates")
movements.append(snatch)

# Cardiovascular and Conditioning
burpee = Exercise("Burpee", 0, 0, "Full Body", "Core, Legs, Shoulders", "Start standing, drop into a push-up, then jump back up to a standing position.", "None")
movements.append(burpee)

jump_rope = Exercise("Jump Rope", 0, 0, "Cardio", "Calves, Shoulders", "Jump over a rope while rotating it with your wrists.", "Jump Rope")
movements.append(jump_rope)

box_jump = Exercise("Box Jump", 0, 0, "Quads", "Glutes, Calves", "Jump from the ground onto a raised platform, then step down.", "Box or Plyo Box")
movements.append(box_jump)

# Chest
decline_bench_press = Exercise("Decline Bench Press", 0, 0, "Chest", "Triceps, Front Deltoids", "Lie on a decline bench, grip the barbell, and press it from your chest to arms fully extended.", "Barbell, Weight Plates, Decline Bench")
movements.append(decline_bench_press)

machine_chest_fly = Exercise("Machine Chest Fly", 0, 0, "Chest", "Front Deltoids", "Sit on a chest fly machine, bring handles together in front of your chest, then slowly return.", "Chest Fly Machine")
movements.append(machine_chest_fly)

# Back
single_arm_lat_pull_down = Exercise("Single Arm Lat Pull Down", 0, 0, "Back", "Biceps", "Sit at a lat pull-down machine with one handle, pull it down to your chest with one arm.", "Lat Pull-Down Machine")
movements.append(single_arm_lat_pull_down)

reverse_fly = Exercise("Reverse Fly", 0, 0, "Back", "Rear Deltoids", "Bend over or use a reverse fly machine to pull dumbbells or handles outward to target rear delts and upper back.", "Dumbbells or Reverse Fly Machine")
movements.append(reverse_fly)

# Shoulders
upright_row = Exercise("Upright Row", 0, 0, "Shoulders", "Traps", "Hold a barbell or dumbbells and pull them up to shoulder height, leading with your elbows.", "Barbell or Dumbbells")
movements.append(upright_row)

scaption = Exercise("Scaption", 0, 0, "Shoulders", "", "Hold dumbbells with palms facing each other, raise arms at a 45-degree angle to shoulder height.", "Dumbbells")
movements.append(scaption)

# Triceps
kickback = Exercise("Tricep Kickback", 0, 0, "Triceps", "", "Bend over with a dumbbell in one hand, extend your arm back to engage the triceps.", "Dumbbell")
movements.append(kickback)

close_grip_push_up = Exercise("Close Grip Push-Up", 0, 0, "Triceps", "Chest", "Perform a push-up with hands close together to target the triceps.", "None")
movements.append(close_grip_push_up)

# Biceps
concentration_curl = Exercise("Concentration Curl", 0, 0, "Biceps", "", "Sit on a bench, brace your elbow on your inner thigh, and curl a dumbbell toward your shoulder.", "Dumbbell")
movements.append(concentration_curl)

incline_dumbbell_curl = Exercise("Incline Dumbbell Curl", 0, 0, "Biceps", "", "Sit on an incline bench, let arms hang down, and curl dumbbells up to shoulder height.", "Dumbbells, Incline Bench")
movements.append(incline_dumbbell_curl)

# Legs (Quads, Hamstrings, Glutes)
step_up = Exercise("Step-Up", 0, 0, "Quads", "Glutes, Hamstrings", "Step onto a raised platform with one leg, then bring the other leg up to meet it.", "Bench or Platform, Dumbbells (optional)")
movements.append(step_up)

pistol_squat = Exercise("Pistol Squat", 0, 0, "Quads", "Glutes", "Perform a squat on one leg while the other leg extends straight out in front of you.", "None (Dumbbells optional for added resistance)")
movements.append(pistol_squat)

good_morning = Exercise("Good Morning", 0, 0, "Hamstrings", "Lower Back, Glutes", "Stand with a barbell on your upper back, hinge at the hips, and lower your torso forward.", "Barbell")
movements.append(good_morning)

glute_kickback = Exercise("Glute Kickback", 0, 0, "Glutes", "Hamstrings", "On all fours or using a cable machine, kick one leg back and up to target the glutes.", "Cable Machine (optional, Dumbbells for bodyweight variation)")
movements.append(glute_kickback)

# Core
hanging_knee_raise = Exercise("Hanging Knee Raise", 0, 0, "Core", "Hip Flexors", "Hang from a bar and lift your knees up toward your chest.", "Pull-up Bar")
movements.append(hanging_knee_raise)

side_plank = Exercise("Side Plank", 0, 0, "Core", "Obliques", "Lie on your side with legs stacked, prop yourself up on one elbow, and hold.", "None")
movements.append(side_plank)

cable_crunch = Exercise("Cable Crunch", 0, 0, "Core", "", "Kneel with a cable behind your head and crunch down to engage the abs.", "Cable Machine")
movements.append(cable_crunch)

ab_rollout = Exercise("Ab Rollout", 0, 0, "Core", "", "Using an ab wheel or barbell, roll out forward while keeping your core tight, then roll back.", "Ab Wheel or Barbell")
movements.append(ab_rollout)

# Additional Conditioning and Full-Body Movements
medicine_ball_slam = Exercise("Medicine Ball Slam", 0, 0, "Full Body", "Core, Shoulders", "Raise a medicine ball overhead and slam it down to the ground with force.", "Medicine Ball")
movements.append(medicine_ball_slam)

battle_rope_wave = Exercise("Battle Rope Wave", 0, 0, "Full Body", "Core, Shoulders", "Grip the ends of battle ropes and create waves by moving your arms up and down.", "Battle Ropes")
movements.append(battle_rope_wave)

tire_flip = Exercise("Tire Flip", 0, 0, "Full Body", "Legs, Back", "Lift a large tire from the ground, using your legs and back, and flip it forward.", "Tire")
movements.append(tire_flip)

sledgehammer_swing = Exercise("Sledgehammer Swing", 0, 0, "Full Body", "Core, Shoulders", "Swing a sledgehammer down onto a tire, alternating sides for a balanced workout.", "Sledgehammer, Tire")
movements.append(sledgehammer_swing)

# Mobility and Stability Exercises
face_down_internal_rotation = Exercise("Face-Down Internal Rotation", 0, 0, "Rotator Cuff", "", "Lie face down, arms at 90 degrees, and rotate them inward to target the rotator cuff.", "None")
movements.append(face_down_internal_rotation)

bird_dog = Exercise("Bird Dog", 0, 0, "Core", "Lower Back, Glutes", "Start on all fours, extend one arm and the opposite leg, hold, then switch sides.", "None")
movements.append(bird_dog)

pallof_press = Exercise("Pallof Press", 0, 0, "Core", "Obliques", "Stand sideways to a cable machine, hold the handle at chest level, and press straight out to resist rotation.", "Cable Machine")
movements.append(pallof_press)
