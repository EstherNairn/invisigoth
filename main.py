import logging
import json
from core import planner, executor, context_builder, generator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    while True:
        goal = planner.get_next_goal()
        if not goal:
            logging.info("No more pending goals. Generating new ones...")
            context = context_builder.build_context()
            raw_goals = generator.generate_goals(context)
            if raw_goals:
                parsed_goals = [planner.Goal.from_dict(g) for g in raw_goals]
                planner.append_pending_goals(parsed_goals)
            goal = planner.get_next_goal()

        if not goal:
            logging.info("Still no goals after fallback. Exiting.")
            break

        executor.execute_goal(goal)
        planner.mark_goal_complete(goal.id)

if __name__ == "__main__":
    main()
