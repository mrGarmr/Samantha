import {Fragment, useEffect, useRef, useState} from "react"
import {useRouter} from "next/router"
import {E, connect, updateState, uploadFiles} from "/utils/state"
import "focus-visible/dist/focus-visible"
import {Badge, Box, Button, Center, Divider, Heading, Image, Input, Text, VStack, useColorMode} from "@chakra-ui/react"
import ReactDropzone from "react-dropzone"
import NextHead from "next/head"

const PING = "http://localhost:8000/ping"
const EVENT = "ws://localhost:8000/event"
const UPLOAD = "http://localhost:8000/upload"
export default function Component() {
const [state, setState] = useState({"answer": "?", "image_made": false, "image_processing": false, "image_url": "", "img": "", "prompt": "", "events": [{"name": "state.hydrate"}], "files": []})
const [result, setResult] = useState({"state": null, "events": [], "processing": false})
const router = useRouter()
const socket = useRef(null)
const { isReady } = router;
const { colorMode, toggleColorMode } = useColorMode()
const Event = events => setState({
  ...state,
  events: [...state.events, ...events],
})
const File = files => setState({
  ...state,
  files,
})
useEffect(() => {
  if(!isReady) {
    return;
  }
  if (!socket.current) {
    connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
  }
  const update = async () => {
    if (result.state != null) {
      setState({
        ...result.state,
        events: [...state.events, ...result.events],
      })
      setResult({
        state: null,
        events: [],
        processing: false,
      })
    }
    await updateState(state, setState, result, setResult, router, socket.current)
  }
  update()
})
return (
<Center sx={{"width": "100%", "height": "100vh", "background": "radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)"}}><VStack><Heading sx={{"fontSize": "1.5em"}}>{`Samantha`}</Heading>
<Divider/>
<ReactDropzone multiple={true}
onDrop={e => File(e)}>{({getRootProps, getInputProps}) => (<Box sx={{"padding": "2em"}}{...getRootProps()}><Input type="file"{...getInputProps()}/>
<Button sx={{"color": "rgb(107,99,246)", "bg": "white", "border": "1px solid rgb(107,99,246)", "width": "80%", "padding": "2em", "margin": "2em"}}>{`Select File`}</Button>
<Text>{`Drag and drop files here or click to select files`}</Text></Box>)}</ReactDropzone>
<Divider/>
<Button onClick={() => uploadFiles(state, result, setResult, state.files, "handle_upload", UPLOAD)}
size="md"
sx={{"width": "60%", "bg": "green", "color": "white", "space": "1em", "margin": "2em"}}>{`Generate Answer`}</Button>
<Divider/>
<Fragment>{state.image_made ? <Fragment><Image src={state.img}
sx={{"height": "18em", "width": "18em"}}/></Fragment> : <Fragment/>}</Fragment>
<Divider/>
<Fragment>{state.image_made ? <Fragment><Badge colorScheme="yellow"
variant="subtle">{`Samantha recognized the image as:`}</Badge></Fragment> : <Fragment/>}</Fragment>
<Fragment>{state.image_made ? <Fragment><Text sx={{"padding": "2em"}}>{state.answer}</Text></Fragment> : <Fragment/>}</Fragment></VStack>
<NextHead><title>{`Samantha`}</title>
<meta content="A Pynecone app."
name="description"/>
<meta content="favicon.ico"
property="og:image"/></NextHead></Center>
)
}