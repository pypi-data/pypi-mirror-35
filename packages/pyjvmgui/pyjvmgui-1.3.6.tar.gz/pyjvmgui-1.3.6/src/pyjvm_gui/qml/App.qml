import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
import QtQuick.Controls.Styles 1.4


RowLayout {

	onWidthChanged:{
		resizeHack.text = "_"
		resizeHack.text = ""
	}
    anchors.fill: parent
    spacing: 5

    Component.onCompleted: {
		bytecodeTable.selection.clear()
		var loc = app.getCurLoc()
		if (loc < bytecodeTable.rowCount) {
			bytecodeTable.selection.select(loc)
			bytecodeTable.positionViewAtRow(loc, ListView.Center)
		}
	}

    Rectangle {
    	id: col1
		Layout.preferredWidth: 500
		Layout.fillHeight: true

		TableView {
			id: bytecodeTable
			selectionMode: SelectionMode.NoSelection
			anchors.fill: parent

			TableViewColumn {
				role: "loc"
				title: "loc"
				width: 50
				movable: false
				resizable: false
			}
			TableViewColumn {
				role: "op"
				title: "Opcode"
				delegate: Text {
					text: styleData.value
					font.family: "monospace"
				}
				width: 150
				movable: false
				resizable: false
			}
			TableViewColumn {
				role: "operands"
				title: "Operands"
				width: 250
				movable: false
				resizable: false
			}

			model: bytecode
		}
	}

    Rectangle {
    	id: col2
		Layout.fillWidth: true
		Layout.alignment: Qt.AlignTop
		Layout.fillHeight: false
		color: "blue"

		ColumnLayout {

			anchors.fill: parent
			spacing: 10

			Button {
				Layout.fillWidth: true
				text: "Step"
				onClicked: {
					app.stepExecutor()
					bytecodeTable.selection.clear()
					var loc = app.getCurLoc()
					if (loc < bytecodeTable.rowCount) {
						bytecodeTable.selection.select(loc)
						bytecodeTable.positionViewAtRow(loc, ListView.Center)
					}
				}
			}
			Button {
				Layout.fillWidth: true
				text: "Step Out"
				onClicked: {
					app.stepOut()
					bytecodeTable.selection.clear()
					var loc = app.getCurLoc()
					if (loc < bytecodeTable.rowCount) {
						bytecodeTable.selection.select(loc)
						bytecodeTable.positionViewAtRow(loc, ListView.Center)
					}
				}
			}
			Button {
				Layout.fillWidth: true
				text: "Step until thread done/blocked"
				onClicked: {
					app.stepUntilDoneOrBlocked()
					bytecodeTable.selection.clear()
					var loc = app.getCurLoc()
					if (loc < bytecodeTable.rowCount) {
						bytecodeTable.selection.select(loc)
						bytecodeTable.positionViewAtRow(loc, ListView.Center)
					}
				}
			}


			Separator {}

			// Frame Information
			Label {
				text: "Frame"
				font.pixelSize: 20
			}
			Text {
				id: idFrameInfo
				text: frameInfo
				Layout.fillWidth: true
				wrapMode: Text.Wrap
			}
			Separator {}

			// Operand stack
			Label {
				text: "Operand stack"
				font.pixelSize: 20
			}
			TableView {
				id: opStackTable
				Layout.fillWidth: true
				selectionMode: SelectionMode.NoSelection
				TableViewColumn {
					role: "operands"
					title: "Operands"
					width: 200
					movable: false
					resizable: false
				}

				model: operandStack
			}

			// Locals Stack
			Label {
				text: "Locals & Args"
				font.pixelSize: 20
			}
			TableView {
				id: localsTable
				Layout.fillWidth: true
				selectionMode: SelectionMode.NoSelection
				TableViewColumn {
					role: "idx"
					title: "Index"
					width: 50
					movable: false
					resizable: false
				}
				TableViewColumn {
					role: "value"
					title: "Value"
					movable: false
					resizable: false
				}

				model: locals
			}

			Text {
				id: resizeHack
				text: ""
				Layout.fillWidth: true
				wrapMode: Text.Wrap
			}
		}
    }
}
