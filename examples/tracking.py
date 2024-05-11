from moovs_business import TrackingFlow, QVideo
import asyncio


async def main():
    # Load detection flow
    tracking = TrackingFlow()

    # Instatiate a video
    video = QVideo("assets/simple-crowd.mp4")

    # Detect all tracks
    track_data = await tracking(video)

    # View the output
    await track_data.view(video, "output.mp4")


asyncio.run(main())
