import asyncio

from moovs_business import PoseFlow, QVideo


async def main():
    # Load detection flow
    pose_estimator = PoseFlow()

    # Instatiate a video
    video = QVideo("assets/surfing.mp4")

    # Do human pose estimation
    pose_data = await pose_estimator(video)

    # View the output
    await pose_data.view(video, "surfing_ai.mp4")


asyncio.run(main())
